from os import path
from subprocess import run as run_command

import click

from .run import run
from .update import update

if not path.exists("/etc/webserver"):
    run_command(["sudo", "mkdir", "-p", "/etc/webserver/dhparams"])
    run_command(["sudo", "mkdir", "-p", "/etc/webserver/letsencrypt"])
    run_command(["sudo", "mkdir", "-p", "/etc/webserver/logs"])
    run_command(["sudo", "mkdir", "-p", "/etc/webserver/static"])
    run_command(["sudo", "mkdir", "-p", "/etc/webserver/conf.d"])


@click.group()
def cli() -> None:
    pass


cli.add_command(run)
cli.add_command(update)

if __name__ == "__main__":
    cli()
