import click

from .utils import explain_step, run_command


@click.group()
def conf() -> None:
    """
    Commands that deal with configurations
    """


@click.command()
@click.argument("domain")
@click.argument("config_file", type=click.Path(exists=True))
def add(domain: str, config_file: str) -> None:
    """
    Adds CONFIG_FILE for DOMAIN
    """
    explain_step("Adding configuration file for website {domain}")
    run_command(f"sudo cp {config_file} /etc/webserver/conf.d/{domain}.conf")
