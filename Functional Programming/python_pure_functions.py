my_list = [1,2,3]

# def add_to_list(item):
#     return my_list.append(item)

# add_to_list(4)



# This is not a pure function. 
# change it to pure function

# make changes to the function 

# def add_to_list(item):
#     my_list.append(item)
#     return my_list

# new_list = add_to_list(4)

# print(my_list)

# print(new_list)

# still above function is not pure as it is refering to the outer list

def add_to_list(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl


new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)