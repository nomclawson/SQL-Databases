# Overview

This program, `recipe_request.py`, is a recipe app. This program allows the user to search recipes using the [Edamam Recipe Search API](https://developer.edamam.com/edamam-docs-recipe-api). The user is then able to save recipes via their URI (recipe ID) in a .db file. Once saved, the user can then retrieve recipes from their saved recipes or using the search feature. 

This program has served me in 3 ways. First, it was a great introduction to the Request module in Python. Second, I was able to learn how to interact with relational databases using SQL commands. And lastly, but most importantly, I am now able to search and save recipes without treading the ad-invested recipe-blogisphere. 

This project pushed me out of my comfort zone but with some time, research, and lots of practice I am very proud of what I have accomplished so far.

[Recipe Database Demo - YouTube](https://youtu.be/LTnlhF0RWXs)

# Relational Database

The database queries were done using the SQLite3 package for Python.

This program currently uses 1 table with columns for:
* ID
* URI (recipe ID from Edamam)
* Label (recipe name)

# Development Environment

This program was developed in Python3 with Visual Studio Code and uses the following libraries:
* SQLite3 
* Random
* Requests
* UrlLib

And the following API:
* [Edamam Search API](https://developer.edamam.com/edamam-docs-recipe-api)

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Edamam Recipe API Documentation](https://developer.edamam.com/edamam-docs-recipe-api)
* [Relational Database Concepts - YouTube](https://www.youtube.com/watch?v=NvrpuBAMddw)
* [Python Requests Library (Guide)](https://realpython.com/python-requests/)
* [SQLite Documentation](https://www.sqlite.org/lang.html)

# Future Work

Future additions include:
* Making GUI (Web App?/TKinter?) especially for my wife
* Edit/remove saved recipes
* Recipe rating
* Add cooking directions in place of link to website 