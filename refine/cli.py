import os
import sys
import click
from .parse import from_spec

@click.command()
@click.argument('dir')
def refine(dir):
    """refine"""
    path = os.path.join(os.getcwd(), dir)
    spec = os.path.join(path, 'spec.yaml')
    sys.path.append(path)
    from_spec(spec)
