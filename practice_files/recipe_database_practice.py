import sqlite3
import random


connection = sqlite3.connect('recipe_practice.db')
cursor = connection.cursor()

def build_tables(cursor):
    command1 = """CREATE TABLE IF NOT EXISTS
    recipes(recipe_id int primary key, recipe_name TEXT, descript text, instructions text)"""
    cursor.execute(command1)
    cmnd2 = """CREATE TABLE IF NOT EXISTS
    recipe_ingredients(recipe_id int primary key, ingredient_id int, quantity_id int, units_id int)"""
    cursor.execute(cmnd2)
    cmnd3 = """CREATE TABLE IF NOT EXISTS
    ingredients(ingredient_id int primary key, ingredient_name text)"""
    cursor.execute(cmnd3)
    cmnd4 = """CREATE TABLE IF NOT EXISTS
    quantity(quantity_id int primary key, quantity_val int)"""
    cursor.execute(cmnd4)
    cmnd5 = """CREATE TABLE IF NOT EXISTS
    units(units_id int primary key, units_name text)"""
    cursor.execute(cmnd5)
#build_tables(cursor)

recipe_ids = set()
ingredient_ids = set()
quantity_ids = set()
units_id = set()

def get_id(ids_set):
    id = random.randint(0000,1000)
    while id in ids_set:
        if id < 1000:
            id += 1
    ids_set.add(id)
    return id


choice = None
while choice != "0":
    print("1) Add recipe")
    print("2) Add ingredient")
    print("3) Add ingredient to recipe")
    print("4) Print all Tables")
    print("5) Print all Grades for a Student")
    print("6) Print all Grades for a Course")
    print("7) Commit changes")
    print("0) Exit ")
    choice = input("> ")
    print()
    if choice == "1":
        # Add New Recipe
        name = input("Recipe name: ")
        description = input("Description: ")
        instructions = input("Instructions: ")
        id = get_id(recipe_ids)
        values = (name, description, instructions,id)
        cursor.execute("INSERT INTO recipes(recipe_name, descript, instructions, recipe_id) VALUES (?,?,?,?)", values)
        cursor.execute("SELECT * FROM recipes")
        result = cursor.fetchall()
        print(result)
        print()
        
    elif choice == "2":
        # Add Ingredient
        name = input("Ingredient: ")
        id = get_id(ingredient_ids)
        values = (name, id)
        cursor.execute("INSERT INTO ingredients (ingredient_name, ingredient_id) VALUES (?,?)", values)
        cursor.execute("SELECT * FROM ingredients")
        result = cursor.fetchall()
        print(result)
        print()

    elif choice == "3":
        # Add ingredient to recipe, with quantity and units
        cursor.execute("SELECT recipe_name FROM recipes")
        result = cursor.fetchall()
        recipe = {}
        count = 1
        for item in result:
            recipe[count] = item[0]
            print(f"{count}) {item[0]}")
            count += 1
        print()
        valid = False
        while not valid:
            num = input("Which recipe would you like to add to? ")
            if num in recipe:
                #    c.execute("SELECT * FROM logins WHERE usernames=(?)", (self.user, ))
                cursor.execute("SELECT recipe_name FROM recipes WHERE recipe_name=(?)", (recipe[num],))
                print(cursor.fetchall())
                
                valid = True

        print()
        

    elif choice == "4":
        print()
        cursor.execute("SELECT * FROM ingredients")
        result = cursor.fetchall()
        print(result)
        print()
        cursor.execute("SELECT * FROM recipes")
        result = cursor.fetchall()
        print(result)
        print()

    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        connection.commit()
        print("Changes committed successfully.")
    elif choice == "0":
        if input("Would you like to commit changes? (y/n): ").lower() == "y":
            connection.commit()



cursor.execute("INSERT INTO ingredients values (?,?)",(random.randint(0000,1000),''))

cursor.execute("SELECT * FROM ingredients")

results = cursor.fetchall()
print(results)
#connection.commit()