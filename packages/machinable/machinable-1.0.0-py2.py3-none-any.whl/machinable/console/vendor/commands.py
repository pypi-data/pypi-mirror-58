import click

from ...project.manager import fetch_imports
from ...project import Project


@click.group(invoke_without_command=True)
@click.pass_context
def vendor(ctx):
    if ctx.invoked_subcommand is not None:
        return

    click.echo(ctx.get_help())


@vendor.command()
def fetch():
    project = Project()
    fetch_imports(project)
    click.echo('Dependencies have been fetched')
