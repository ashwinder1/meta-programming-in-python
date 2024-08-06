menu = ["espresso", "mocha", "latte", "cappucino", "cortado", "americano"]

# function to select the words starting with letter c
def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee
    
# use of map function
# map_coffee = map(find_coffee, menu)

# print(map_coffee)

# for x in map_coffee:
#     print(x)

filter_coffee = filter(find_coffee, menu)

print(filter_coffee)

for x in filter_coffee:
    print(x)
