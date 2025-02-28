import click

# subtle bug that may burn you
var=[]
var


@click.command()
@click.option(
    "--phrase",
    prompt="Enter a phrase",
    help="Phase in a phrase to tokenize: i.e. The Whale is large",
)
def tokenize(phrase):
    """This is a commandline tool that tokenizes phrases"""

    click.style(click.style('ATTENTION', blink=True, bold=True))

    click.echo(click.style(f"tokenized phrase: {phrase.split()}", bg='yellow', fg='white'))


if __name__ == "__main__":
    tokenize()
