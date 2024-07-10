user_num1 = input('First number is: ')
user_num2 = input('Second number is: ')
user_sum = float(user_num1) + float(user_num2)
print(user_sum)

n1 = input('First float number is: ')
n2 = input('Second float number is:')
sum = float(n1) + float(n2)

#print("the sum of the numbers" + n1 + n2 + "is" + sum) ## gives type error  ##implicit conversion doesn't work
# on string and float

print("the sum of the numbers " + str(n1) + " and " + str(n2) + " is " + str(sum))
