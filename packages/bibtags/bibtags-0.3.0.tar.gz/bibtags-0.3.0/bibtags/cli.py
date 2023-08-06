"""Console script for bibtags."""
import sys
import click

from bibtags import cite as bt_cite

@click.group()
def main(args=None):
    """Console script for bibtags."""
    return 0

@main.command()
@click.argument("tags", nargs=-1)
def cite(tags):
    """Console script for bibtags."""
    click.echo("tags: {}".format(tags))
    click.echo(bt_cite(*tags))
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
