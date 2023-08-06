from importlib.resources import path

import click

from .utils import run_command, explain_step


# pylint: disable=no-value-for-parameter
@click.command()
@click.argument("domain")
def genconf(domain: str) -> None:
    """
    Create HTTPS configuration file with examples for DOMAIN
    """
    explain_step(f"HTTPS configuration file for website {domain}:")
    with path(package="webserver", resource="config") as folder:
        run_command(f'cat {folder}/443-template.conf {folder}/examples/* | sed "s/{{{{SERVER_NAME}}}}/{domain}/g"')
        click.echo("}")


if __name__ == "__main__":
    genconf()
