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
from Food_utilities import read_food

k = read_food("Spanakopita|5|True|260")

print(k.__str__())

t = Food("blank", 5, True, 0)
