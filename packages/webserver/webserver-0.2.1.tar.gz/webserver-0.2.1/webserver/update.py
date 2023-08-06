from subprocess import run

import click

from .utils import explain_step


# pylint: disable=no-value-for-parameter
@click.command()
def update() -> None:
    """
    Run Highly-Available nginx:mainline-alpine stack
    """
    explain_step("Updating images of webserver Docker Swarm stack")
    run(
        [
            "sudo",
            "docker",
            "service",
            "update",
            "--image",
            "nginx:mainline-alpine",
            "webserver_nginx",
        ],
        check=True,
    )


if __name__ == "__main__":
    update()
