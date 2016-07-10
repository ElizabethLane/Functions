# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def total_item_cost(cost, state_name, tax = 0.05):
    if state_name == "CA":
        tax = 0.07
        item_with_tax = cost + cost * tax
    else:
        item_with_tax = cost + cost * tax

    return item_with_tax




#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def is_berry(fruit_name):
    if type(fruit_name) == str and fruit_name == "strawberry" or fruit_name == "cherry" or fruit_name == "blackberry":
        return True
    else:
        return False

def shipping_cost(fruit_name):
    if type(fruit_name) == str:
        if is_berry(fruit_name) == True:
            return "0"
        elif is_berry(fruit_name) == False:
            return "5"

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_hometown(town_name):
    if type(town_name) == str:
        if town_name == "Walnut":
            return True
        else:
            return False

def full_name(first_name, last_name):
    if type(first_name) == str and type(last_name) == str:
        return first_name + " " + last_name

def hometown_greeting(home_town, first_name, last_name):
    if is_hometown(home_town) == True:
        user_greeting = "Hi, " + full_name(first_name, last_name) + ", " + \
        "we're from the same place!"
    elif is_hometown(home_town) == False:
        user_greeting = "Hi, " + full_name(first_name, last_name) + ", " + \
        "where are you from?"
    print user_greeting


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def increment(x = 1):
    def add(y):
        return x + y
    return add


addfive = increment(5)
addfive(5)
addfive(20)

def add_numbers(numbers_list, num):
    if type(numbers_list) == list:
        numbers_list.append(num)
    return numbers_list



#####################################################################