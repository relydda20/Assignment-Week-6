inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

#Appending pocket into inventory using keys()
inventory['pocket'] = 'seashell', 'strange berry', 'lint'

#Sorting the items in backpack
inventory['backpack'].sort()

#Removing dagger from backpack
inventory['backpack'].remove('dagger')

#Appending 50 gold to the total
inventory['gold']+50

#Printing all of the changes
print(inventory)