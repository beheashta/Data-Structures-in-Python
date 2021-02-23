"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Beheashta Atchekzai
ID:     190637520
Email:  atch7520@mylaurier.ca
__updated__ = "2020-01-16"
------------------------------------------------------------------------
"""

from Food_utilities import get_vegetarian, read_foods

fv = open("foods.txt", "r")

foods = read_foods(fv)

v = get_vegetarian(foods)

for i in v:
    print(i.__str__())
    print("----------------------")
