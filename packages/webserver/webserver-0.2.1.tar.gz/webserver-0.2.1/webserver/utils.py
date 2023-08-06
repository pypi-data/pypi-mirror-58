import click


def explain_step(explanation: str) -> None:
    click.echo(click.style(explanation, fg='green'))
