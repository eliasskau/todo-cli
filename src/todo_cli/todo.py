import click
import sqlite3

con = sqlite3.connect("data/todo.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS todo(item)")

@click.group()
def main():
    """ A private cli to do list"""
    pass

@main.command()
@click.option('--item',prompt='Add an item to your todo list',help='Add items to a todo SQLite database')
def add(item):
    cur.execute("""INSERT INTO todo VALUES (?),item""")
    con.commit()

@main.command()
def list():
    for row in cur.execute("SELECT item FROM todo"):
        print(row)



if __name__ == "__main__":
    main()