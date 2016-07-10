
# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################

# def increment(x= 1):
#     def add(y):
#         return x * y
#     return add


# addfive = increment(5)
# addfive(5)
# addfive(20)

def add_numbers(numbers_list, num):
    if type(numbers_list) == list:
        numbers_list.append(num)
    return numbers_list


print add_numbers([3,2,1], 4)