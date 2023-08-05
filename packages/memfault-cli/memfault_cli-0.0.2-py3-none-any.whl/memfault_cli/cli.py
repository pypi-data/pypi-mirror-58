import logging
import os
from typing import Type

import click

from memfault_cli.upload import (
    BugreportUploader,
    CoredumpUploader,
    SoftwareArtifactUploader,
    SymbolUploader,
    Uploader,
    upload_all,
)


class MemfaultCliClickContext(object):
    """
    A context passed around between the memfault cli sub-commands.


    If the top level CLI has any "required" it's not possible to display
    any help info about the subcommands using "--help" without providing them.
    By passing around this context, subcommand help messages can be displayed
    and errors can be raised in a uniform way
    """

    def __init__(self):
        self.obj = {}

    def _find_obj_or_raise(self, name):
        value = self.obj.get(name)
        if not value:
            raise click.exceptions.UsageError(f'Missing option "--{name}".')
        return value

    @property
    def org(self):
        return self._find_obj_or_raise("org")

    @property
    def project(self):
        return self._find_obj_or_raise("project")

    @property
    def email(self):
        return self._find_obj_or_raise("email")

    @property
    def password(self):
        return self._find_obj_or_raise("password")

    @property
    def software_info(self):
        sw_type = self.obj.get("software_type")
        sw_ver = self.obj.get("software_version")
        if sw_type is None and sw_ver is None:
            return None

        if sw_type is None or sw_ver is None:
            raise click.exceptions.UsageError(
                f'"--software_version" and "--software_type" must be specified together'
            )

        return (sw_type, sw_ver)

    @property
    def file_url(self):
        FILES_BASE_URL = "https://files.memfault.com"
        url = self.obj.get("url")
        if url is None:
            return FILES_BASE_URL
        return url


pass_memfault_cli_context = click.make_pass_decorator(
    MemfaultCliClickContext, ensure=True
)


@click.group()
@click.option("--email", help="Account email to authenticate with")
@click.password_option(
    "--password",
    prompt=False,
    help="Account password or user API key to authenticate with",
)
@click.option("--org", help="Organization slug")
@click.option("--project", help="Project slug")
@click.option("--url", hidden=True)
@pass_memfault_cli_context
def cli(ctx: MemfaultCliClickContext, **kwargs):
    ctx.obj.update(kwargs)


def _do_upload_all(
    ctx: MemfaultCliClickContext, path: str, uploader_cls: Type[Uploader],
):
    upload_all(
        ctx.org,
        ctx.project,
        path,
        (ctx.email, ctx.password),
        ctx.software_info,
        ctx.file_url,
        uploader_cls,
    )


@cli.command(name="upload-coredump")
@click.argument("path")
@pass_memfault_cli_context
def upload_coredump(ctx: MemfaultCliClickContext, path: str):
    """Upload a firmware coredump for analysis.

    Coredumps can be added to a firmware platform by integrating the Memfault C SDK:
    https://github.com/memfault/memfault-firmware-sdk
    """
    _do_upload_all(ctx, path, CoredumpUploader)


@cli.command(name="upload-bugreport")
@click.argument("path")
@pass_memfault_cli_context
def upload_bugreport(ctx: MemfaultCliClickContext, path: str):
    """Upload an Android Bug Report for analysis by Memfault."""
    _do_upload_all(ctx, path, BugreportUploader)


@cli.command(name="upload-symbols")
@click.option(
    "--software-type",
    required=False,
    help="Required for firmware builds, see https://mflt.io/34PyNGQ",
)
@click.option(
    "--software-version",
    required=False,
    help="Required for firmware builds, see https://mflt.io/34PyNGQ",
)
@click.argument("path")
@pass_memfault_cli_context
def upload_symbols(ctx: MemfaultCliClickContext, path: str, **kwargs):
    """Upload symbols for a Firmware or Android build."""
    ctx.obj.update(**kwargs)

    if ctx.software_info is None:
        uploader = SymbolUploader
    else:
        uploader = SoftwareArtifactUploader
        if os.path.isdir(path):
            raise click.exceptions.UsageError(
                f"{path} is a directory but must be a file"
            )

    _do_upload_all(ctx, path, uploader)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    cli()


if __name__ == "__main__":
    main()
