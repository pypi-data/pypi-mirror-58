import click

from .constants import (CLI_SERVICE_SPLASH, AVAILABLE_TEMPLATES, AVAILABLE_INFRA)


@click.group()
@click.pass_context
def services(ctx):
    click.echo(CLI_SERVICE_SPLASH)


@services.command()
@click.argument('template', nargs=1, type=str)
@click.option('-d', '--dest', nargs=1, type=str, default=None)
def new_service(template: str, dest: str) -> None:
    """Supported Templates: Flask, Django."""
    template = template.lower()
    try:
        AVAILABLE_TEMPLATES[template](**{
            'destination': dest or '.'
        })
    except KeyError:
        click.echo(f'Unsupported template "{template}". {new_service.__doc__}')
        exit(1)


@services.command()
@click.argument('infra', nargs=1, type=str)
def big_bang(infra):
    """Available Infra: Super-Jopi."""
    infra = infra.lower()
    try:
        AVAILABLE_INFRA[infra]()
    except KeyError:
        click.echo(f'Unsupported infra: "{infra}". {big_bang.__doc__}')
        exit(1)
