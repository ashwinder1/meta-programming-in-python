#simple for loop with range

for i in range(10):
    print('Looping ....', i)

# looping is used to iterate through the sequence and access each item in it

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramsu', 'Chocolate Cake']

for item in favorites:
    print('I like this desert : ', item)

# in the standard for loop we don't have access to the index
# we can use the enumerate function to do this

for idx, item in enumerate(favorites):
    print(idx, item)

# functioning of while loop

count = 0

while count < len(favorites):
    print('I like this desert', favorites)

count += 1

