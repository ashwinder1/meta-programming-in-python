# String Reversal

# Two ways

# Using slice function
# Syntax of slice function str[start:stop:step]

trial = "reversal"

reversed_string = trial[::-1]
# Traverse string from the right to left, one index position at a time

print(reversed_string)

# Using Recursion

def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:]) + str[0]
    
str = "reversal"

reverse = string_reversal(str)
print(reverse)


# Slicing Function Working
# letters = "AaBbCcDd"

## Get all characters relying on default offsets
# letters[::]
# 'AaBbCcDd'
# letters[:]
# 'AaBbCcDd'

# # Get every other character from 0 to the end
# letters[::2]
# 'ABCD'

# >>> # Get every other character from 1 to the end
# letters[1::2]
# 'abcd'