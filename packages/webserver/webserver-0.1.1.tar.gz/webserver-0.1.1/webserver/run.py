from importlib.resources import path
from subprocess import run as run_command

import click


# pylint: disable=no-value-for-parameter
@click.command()
@click.option("--config", help="Path to with environment configuration")
def run(config: str) -> None:
    """
    Run Highly-Available nginx:mainline-alpine stack
    """
    click.echo('Creating shared "nginx" network (if not created)')
    run_command(
        [
            "sudo",
            "docker",
            "network",
            "create",
            "-d",
            "overlay",
            "--attachable",
            "nginx",
        ]
    )

    click.echo('Creating "nginx-static" and "nginx-conf" volumes (if not created)')
    run_command(
        [
            "sudo",
            "docker",
            "volume",
            "create",
            "--driver",
            "local",
            "--opt",
            "type=none",
            "--opt",
            "device=/etc/webserver/static",
            "--opt",
            "o=bind",
            "--name",
            "nginx-static",
        ]
    )
    run_command(
        [
            "sudo",
            "docker",
            "volume",
            "create",
            "--driver",
            "local",
            "--opt",
            "type=none",
            "--opt",
            "device=/etc/webserver/conf.d",
            "--opt",
            "o=bind",
            "--name",
            "nginx-conf",
        ]
    )

    click.echo('Pulling nginx:mainline-alpine image and deploying to Docker Swarm')
    run_command(["sudo", "docker", "pull", "nginx:mainline-alpine"], check=True)
    with path(package="webserver", resource="config") as folder:
        run_command(
            [
                "sudo",
                "docker",
                "stack",
                "deploy",
                "-c",
                f"{folder}/integrated.yml",
                "webserver",
            ],
            check=True,
        )


if __name__ == "__main__":
    run()
