groceries = ["banana","orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#Defining the function to subtract present stock and to check for empty stock
def compute_bill(food):
    total = 0
    for i in food:
        if stock[i] > 0:
            total += prices[i]
            stock[i]-= 1
    return total

#Recalling def function with groceries in it
print("Final price:", compute_bill(groceries))