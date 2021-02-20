import sqlite3


connection = sqlite3.connect('recipe_demo.db')
cursor = connection.cursor()



command1 = """CREATE TABLE IF NOT EXISTS
recipes(recipe_name TEXT PRIMARY KEY, ingredients text)"""
cursor.execute(command1)


cmnd2 = """CREATE TABLE IF NOT EXISTS
ingredients(recipe_name text primary key, ingredient TEXT, quantity int, units text)"""
cursor.execute(cmnd2)

cursor.execute("INSERT INTO ingredients values ( 'beef', 1, 'lbs')")
cursor.execute("INSERT INTO ingredients values ( 'carrots', .5, 'lbs')")
cursor.execute("INSERT INTO ingredients values ( 'broth', 16, 'oz')")
cursor.execute("INSERT INTO ingredients values ( 'broccoli',.5,'lbs')")


cursor.execute("INSERT INTO recipes VALUES ('Beef Stew', 'beef, broth, carrots, broccoli')")
cursor.execute("INSERT INTO recipes VALUES ('Fried Rice', 'Jasmine rice, water, oil, egg, (veggies)')")
cursor.execute("INSERT INTO recipes VALUES ('Breakfast Burrito', 'tortillas, sausage, egg, cheese, hashbrowns')")

cursor.execute("SELECT * FROM ingredients")

results = cursor.fetchall()
print(results)