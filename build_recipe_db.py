"""
Build the recipe Database for recipe_request.py
"""
import sqlite3 as sql

def get_filename():
    FILENAME = input("Please enter database filename: ")
    if ".db" not in FILENAME:
        FILENAME += ".db"
    return FILENAME

def create_table(filename):
    con = sql.connect(filename)
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS recipes (id int primary key, uri text, directions text, label text)")

    c.execute("SELECT * FROM recipes")
    result = c.fetchall()
    print(result)


def build():
    filename = get_filename()
    create_table()

build()