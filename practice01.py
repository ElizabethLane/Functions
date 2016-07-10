
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def item_cost(cost, state_name, tax = 0.05):
    if state_name == "CA":
        tax = 0.07
        item_with_tax = cost * tax
    else:
        item_with_tax = cost * tax

    return item_with_tax


print item_cost(2, "AZ" , 0.09)