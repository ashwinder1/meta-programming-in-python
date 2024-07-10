# Algorithm for a palindrome

# Input: string

# takes input string and return true if the string is a palindrome else false

#isPalinderome("racecar")
# > True 

# Returns: Boolean

# def isPalindrome(str):
#     start_index = 0
#     end_index = len(str) - 1

#     for x in str:
#         if str[start_index] != str[end_index]:
#             return False
#     return True



n = len(str)
def isPalindrome(str):
    for i in range(n//2):
        if(str[i] != str[n - i - 1]):
            return False
    return True

print(isPalindrome('racecar'))


