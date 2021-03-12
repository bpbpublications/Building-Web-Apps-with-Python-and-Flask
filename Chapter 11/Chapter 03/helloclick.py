import click

@click.command()
def hello():
    click.echo('HelloClick!')
    if __name__ == '__main__':
        hello()
