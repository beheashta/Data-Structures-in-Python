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

from Food import Food
from Food_utilities import write_foods

fv = open("foods.txt", "w")

k = Food("Biryani", 2, False, 130)
y = Food("Beaver Tail", 0, True, 500)

l = [k, y]

write_foods(fv, l)

