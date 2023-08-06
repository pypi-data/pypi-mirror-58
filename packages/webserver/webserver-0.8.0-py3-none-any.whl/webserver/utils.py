from subprocess import DEVNULL, CalledProcessError, run
from sys import exit

import click


def explain_step(explanation: str, quiet: bool = False) -> None:
    if quiet:
        return

    click.echo(click.style(explanation, fg="green"))


def explain_error(explanation: str) -> None:
    click.echo(click.style(explanation, fg="red"))


def run_command(
    command: str,
    quiet: bool = False,
    check: bool = False,
    error_message: str = "Error!",
) -> None:
    try:
        run(
            command,
            shell=True,
            check=check,
            stdout=DEVNULL if quiet else None,
            stderr=DEVNULL if not check and quiet else None,
        )
    except CalledProcessError:
        if check:
            explain_error(error_message)
            exit(1)


def docker(
    command: str,
    quiet: bool = False,
    check: bool = False,
    error_message: str = "Error!",
) -> None:
    run_command(
        f"sudo docker {command}", quiet=quiet, check=check, error_message=error_message
    )
