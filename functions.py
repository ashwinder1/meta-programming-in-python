# def first_function():
#     return print("first function")

# first_function();


# bill = 175.00

# tax_rate = 15

# total_tax = (bill * tax_rate)/100.00

# print("Total tax is: ", total_tax)


# functions are reusable pieces of code that makes program modular

def calculate_tax(bill, tax_rate):
    return round((bill*tax_rate)/100.00,2)

print("Total tax: ", calculate_tax(175.00, 15))
