import click

@click.group()
def Welcome():
    click.echo("Welcome to Click!")

@click.command()
@click.argument('name')
def greetings(name):
    click.echo('Hello {}'.format(name))

@click.command()
def goodbye(name):
    click.echo('Goodbye {}'.format(name))

Welcome.add_command(greetings)
Welcome.add_command(goodbye)
if __name__ == '__main__':
    Welcome()
