import logging
import os
import re
from abc import abstractmethod
from typing import Any, Generator, Optional, Tuple, Type

import requests
from elftools.elf.elffile import ELFFile
from requests import Response

from .gnu_build_id import get_gnu_build_id

LOG = logging.getLogger(__name__)

GNU_BUILD_ID_RE = re.compile(r"Build ID: (?P<gnu_build_id>[a-f\d]+)")


def check_response(response: Response):
    if response.status_code >= 400:
        raise Exception(
            f"Request failed with HTTP status {response.status_code}\nResponse body:\n{response.content.decode()}"
        )


class Uploader:
    def __init__(
        self,
        file_path: str,
        org: str,
        project: str,
        account: Tuple[str, str],
        base_url: str,
        software_info: Optional[Tuple[str, str]],
    ):
        self.file_path = file_path
        self.org = org
        self.project = project
        self.account = account
        self.software_info = software_info
        self.base_url = base_url

    def _projects_base_url(self) -> str:
        return (
            f"{self.base_url}/api/v0/organizations/{self.org}/projects/{self.project}"
        )

    @abstractmethod
    def can_upload_file(self) -> bool:
        pass

    @abstractmethod
    def entity_url(self) -> str:
        pass

    def _is_already_uploaded(self) -> bool:
        return False

    def _prepare_upload(self) -> Tuple[str, str]:
        response = requests.post(
            f"{self._projects_base_url()}/upload", auth=self.account
        )
        check_response(response)
        data = response.json()["data"]
        return data["upload_url"], data["token"]

    def _put_file(self, upload_url: str) -> None:
        with open(self.file_path, "rb") as file:
            check_response(requests.put(upload_url, data=file))

    def _post_token(self, token: str) -> None:
        json_d = {"file": {"token": token}}
        if self.software_info:
            software_type, software_version = self.software_info
            json_d["software_version"] = {
                "version": software_version,
                "software_type": software_type,
            }
        check_response(
            requests.post(self.entity_url(), auth=self.account, json=json_d,)
        )

    def _is_elf(self) -> Tuple[bool]:
        with open(self.file_path, "rb") as file:
            if file.read(4) != b"\x7FELF":
                return False

        return True

    def _get_gnu_build_id_and_has_debug_info(self) -> Tuple[Optional[str], bool]:
        with open(self.file_path, "rb") as f:
            elf = ELFFile(f)
            return get_gnu_build_id(elf), elf.has_dwarf_info()

    def upload(self) -> None:
        if self._is_already_uploaded():
            LOG.info(f"{self.file_path}: skipping, already uploaded.")
            return
        upload_url, token = self._prepare_upload()
        self._put_file(upload_url)
        self._post_token(token)
        LOG.info(f"{self.file_path}: uploaded!")


class BugreportUploader(Uploader):
    def can_upload_file(self) -> bool:
        if not self.file_path.endswith(".zip"):
            return False
        LOG.info(f"{self.file_path}: ends with .zip: this is an Android bugreport.zip")
        return True

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/bugreports"


class CoredumpUploader(Uploader):
    def can_upload_file(self) -> bool:
        with open(self.file_path, "rb") as f:
            hdr = f.read(4).decode("ascii", errors="ignore")
            if hdr != "CORE":
                LOG.error(f"{self.file_path} is not a Memfault Coredump")
                return False

        return True

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/coredumps"


class SymbolUploader(Uploader):
    gnu_build_id: str = ""

    def can_upload_file(self) -> Optional[Any]:
        if not self._is_elf():
            LOG.info(f"{self.file_path}: Not an ELF file")
            return False

        self.gnu_build_id, has_debug_info = self._get_gnu_build_id_and_has_debug_info()
        if not self.gnu_build_id:
            LOG.info(
                f"{self.file_path}: looks like an ELF but does not contain a GNU Build ID"
            )
            return False
        if not has_debug_info:
            LOG.info(f"{self.file_path}: looks like an ELF but it has no .debug_info")
            return False
        LOG.info(
            f"{self.file_path}: ELF file with .debug_info and GNU Build ID: {self.gnu_build_id}"
        )
        return True

    def _is_already_uploaded(self) -> bool:
        response = requests.head(
            f"{self._projects_base_url()}/symbols-by-gnu-build-id/{self.gnu_build_id}",
            auth=self.account,
        )
        try:
            check_response(response)
        except:
            if response.status_code == 404:
                return False
            raise
        return True

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/symbols"


class SoftwareArtifactUploader(Uploader):
    def can_upload_file(self) -> Optional[Any]:
        if not self._is_elf():
            LOG.info(f"{self.file_path}: Not an ELF file")
            return False

        self.gnu_build_id, has_debug_info = self._get_gnu_build_id_and_has_debug_info()
        if not self.gnu_build_id:
            # We can handle a symbol artifact without a Build ID but might as well
            # recommend it!
            LOG.info(
                f"{self.file_path}: Consider adding a GNU Build ID to uniquely identify the build"
            )

        if not has_debug_info:
            LOG.info(f"{self.file_path}: looks like an ELF but it has no .debug_info")
            return False
        LOG.info(f"{self.file_path}: ELF file with .debug_info")
        return True

    def _is_already_uploaded(self) -> bool:
        return False

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/symbols"


def try_upload(
    org: str,
    project: str,
    file_path: str,
    account: Tuple[str, str],
    software_info: Optional[Tuple[str, str]],
    base_url: str,
    uploader_cls,
):
    uploader = uploader_cls(file_path, org, project, account, base_url, software_info)
    if uploader.can_upload_file():
        uploader.upload()
        return
    LOG.info(f"{file_path}: skipping...")


def walk_files(root: str) -> Generator[str, Any, Any]:
    for root, dirs, files in os.walk(root):
        yield from map(lambda file: os.path.join(root, file), files)


def upload_all(
    org: str,
    project: str,
    starting_path: str,
    account: Tuple[str, str],
    software_info: Optional[Tuple[str, str]],
    base_url: str,
    uploader_cls: Type[Uploader],
) -> None:
    if os.path.isdir(starting_path):
        print(starting_path)
        for file in walk_files(starting_path):
            try_upload(
                org, project, file, account, software_info, base_url, uploader_cls
            )
    else:
        try_upload(
            org, project, starting_path, account, software_info, base_url, uploader_cls
        )
