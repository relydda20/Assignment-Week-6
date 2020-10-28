prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = 5

#Displaying data in the given format
for x,y in prices.items():
    print(x)
    print("price:", y)
    print("stock:", stock)

#Counting total cost given a stock
total = 0
for item in prices:
    total += stock * prices[item]
print("The total price is:", total)