# Using open function

file = open("test.txt", mode = 'r')

data = file.readline()

print(data)

file.close()

# Using with open function

with open('test.txt', mode = 'r') as file:
    data = file.readline

print(data)

# creating file

with open('newfile.txt', 'w') as file:
    file.write('This is a new file created!')

# for multiple lines and appending instead of overwriting the file
#using list to write multiple lines

try:
    with open('newfile.txt', 'a') as file:
        file.writelines(['this is the first line', '\nthis is second line', '\n this is third line'])
except FileNotFoundError as e:
    print("Error", e)

with open('test.txt', 'r') as file:
    #data = file.readlines()
    #print(data)
    for x in file:
        print(x)