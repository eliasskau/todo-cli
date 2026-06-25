import click

@click.group()
def main():
    """ A private cli to do list"""
    pass
@click.command()
@click.option('--num',prompt='How much do you have to do?',help='How many todos does the user have')
def todo(num):
    click.echo(f"You have {num} things to do")




if __name__ == "__main__":
    main()