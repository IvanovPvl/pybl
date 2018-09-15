import click

from blockchain import Blockchain
from proof_of_work import ProofOfWork


class Cli:
    bc = None

@click.group()
@click.pass_context
def main(ctx = None):
    """Simple CLI for blockchain interaction."""

    ctx.obj = Cli()

@main.command()
@click.argument('data')
@click.pass_obj
def add_block(cli, data):
    """Add block to blockchain."""

    if cli.bc == None:
        cli.bc = Blockchain()

    cli.bc.add_block(data)

@main.command()
@click.pass_obj
def print_blockchain(cli):
    """Print blockchain."""

    for b in cli.bc:
        print(b)
        print()

if __name__ == '__main__':
    main()
