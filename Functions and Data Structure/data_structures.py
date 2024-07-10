menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

order = [
    {"name": 'espresso',
        "price": 1.99},
    {"name": 'coffee', 
        "price": 2.50},
    {"name": 'cake', 
        "price": 2.79},
    {"name": 'soup', 
        "price": 4.50},
    {"name": 'sandwich',
        "price": 4.99}
]

total_bill = 0
for item in order:
    total_bill += item["price"]

print(f"Total bill: ${total_bill:.2f}")


# functions of list
new_list = [1,2,3,4]

new_list.insert(0,0)

new_list.extend(new_list)

print(new_list)