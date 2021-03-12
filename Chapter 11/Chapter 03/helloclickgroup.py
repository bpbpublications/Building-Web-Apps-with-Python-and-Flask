import click

@click.group()
def Welcome():
    click.echo("Welcome to Click!")

@click.command()
def greetings():
    click.echo('Hello user')

@click.command()
def goodbye():
    click.echo('Goodbye user')

hello.add_command(greetings)
hello.add_command(goodbye)
if __name__ == '__main__':
    Welcome()
