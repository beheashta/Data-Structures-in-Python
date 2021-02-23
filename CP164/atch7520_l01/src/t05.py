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

from Food_utilities import read_foods

fv = open("Foods.txt", "r")

foods = read_foods(fv)

for i in foods:
    print(i.__str__())
    print("------------------------------")
