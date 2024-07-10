loyalty_customer = True
total_bill = 210

if loyalty_customer and total_bill > 100 :
    # give 20% discount
    total_bill = total_bill - float(total_bill/100) * 20
elif total_bill > 100 :
    # give 10% discount
    total_bill = total_bill - float(total_bill/100) * 10
else :
    # sorry no discount, 5% service charge applied
    print("Sorry, no discount ...")

print("Total Bill: ", float(total_bill))

## variable current  keeps track of the state of the light - on or off.
current = False

if current:
    current = False
    print('Turning lights off!')

# if not current:
#     current = True
#     print('Turning lights on!')

if current:
    current = False
    print('Turning lights off!')
else :
    current : True
    print('Turning lights on!')