from os import path
from subprocess import run as run_command

import click

from .run import run
from .update import update
from .genconf import genconf

if not path.exists("/etc/webserver"):
    click.echo("Initializing /etc/webserver directory")
    for folder in ("dhparams", "letsencrypt", "logs", "static", "conf.d"):
        run_command(["sudo", "mkdir", "-p", f"/etc/webserver/{folder}"])


@click.group()
def cli() -> None:
    pass


@click.group()
def sites() -> None:
    pass


sites.add_command(genconf)

cli.add_command(run)
cli.add_command(update)
cli.add_command(sites)

if __name__ == "__main__":
    cli()
