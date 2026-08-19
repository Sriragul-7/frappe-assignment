import click

@click.command()
def cmd():
    click.echo("Hello from the custom Bench CLI!!")
    
commands = [cmd]