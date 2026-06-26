import click
import sqlite3

con = sqlite3.connect("data/todo.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY,item)")

@click.group()
def main():
    """ A private cli to do list"""
    pass

@main.command()
@click.argument('item', type=str)
def add(item):
    cur.execute("INSERT INTO todo (item) VALUES (?)",(item,))
    con.commit()
    con.close()

@main.command()
@click.argument('id', type=int)
def delete(id):
    cur.execute("DELETE FROM todo WHERE id=?", (id,))
    con.commit()
    con.close()

@main.command()
def list():
    for row in cur.execute("SELECT item FROM todo"):
        print(row)



if __name__ == "__main__":
    main()