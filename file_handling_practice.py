# finding a new random name for the new pet dog

import random

f = open('petnames.txt', 'r')
# read the content of file
file_content = f.read()
#get the f_content variable into a list. 
f_content_list = file_content.split("\n")
f.close()
print(random.choice(f_content_list))


