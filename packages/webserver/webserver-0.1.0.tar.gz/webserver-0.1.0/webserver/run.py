import click
import importlib.resources as pkg_resources
from subprocess import run as run_command

# pylint: disable=no-value-for-parameter
@click.command()
@click.option("--config", help="Path to with environment configuration")
def run(config: str):
    """
    Run Highly-Available nginx:mainline-alpine stack
    """
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
    # run_command(['sudo', 'docker', 'pull', 'nginx:mainline-alpine'], check=True)
    with pkg_resources.path(package="webserver", resource="config") as path:
        run_command(
            [
                "sudo",
                "docker",
                "stack",
                "deploy",
                "-c",
                f"{path}/integrated.yml",
                "webserver",
            ],
            check=True,
        )


if __name__ == "__main__":
    run()
