"""
-------------------------------------------------------
Food class utility functions.
-------------------------------------------------------
Author:  Beheashta Atchekzai
ID:      190637520
Email:   atch7520@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-23"
-------------------------------------------------------
"""

from copy import deepcopy

from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    n = input("Enter Name:")
    
    print("Origin")
    
    # Create food object to use the origins function
    p = Food("Butter Chicken", 2 , True, 120)
    print(p.origins())
    
    o = int(input(":"))
    v = input("Vegetarian (Y/N):")
    if v == "Y":
        v = True
    
    if v == "N":
        v = False
        
    c = int(input("Calories:"))
    
    food = Food(n, o, v == True, c)

    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    line.strip()
    x = line.split("|")
    
    if x[2] == "True":
        x[2] = True
    if x[2] == "False":
        x[2] = False
        
    origin = int(x[1])
    
    food = Food(x[0], origin, x[2] , int(x[3]))

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    x = file_variable.readline()
    
    while x != "":
        i = read_food(x)
        
        foods.append(i)
        
        x = file_variable.readline()

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    for x in foods:
        line = "{}|{}|{}|{}\n".format(x.name, x.origin, x.is_vegetarian, x.calories)
        file_variable.write(line)

    return None


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    foods_copy = deepcopy(foods)
    
    veggies = []
    
    for x in foods_copy:
        if x.is_vegetarian == True:
            veggies.append(x)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    --------------------------------$-----------------------
    """
    assert origin in range(len(Food.ORIGIN))
    
    foods_copy = deepcopy(foods)
    origins = []
    for x in foods_copy:
        if x.origin == origin:
            origins.append(x)

    return(origins)


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    foods_copy = deepcopy(foods)
    tot = 0 
    counter = 0 
    
    for x in foods_copy:
        tot += x.calories
        counter += 1 
    
    avg = tot // counter

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    foods_copy = deepcopy(foods)
    tot = 0 
    counter = 0 
    
    for x in foods_copy:
        if x.origin == origin:
            tot += x.calories
            counter += 1 
    
    avg = tot // counter

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    foods_copy = deepcopy(foods)
    foods_copy.sort()
    print("Food                                Origin       Vegetarian Calories\n----------------------------------- ------------ ---------- --------")
    for i in foods_copy:
        print("{:<35} {:<12} {:>10} {:>8}".format(i.name, Food.ORIGIN[i.origin], str(i.is_vegetarian), i.calories))
    
    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    
    foods_copy = deepcopy(foods)
    result = []
    
    for item in foods_copy:
        if origin == item.origin: 
            if max_cals >= item.calories or max_cals == 0:
                if is_veg == False:
                    result.append(item)

    return result
