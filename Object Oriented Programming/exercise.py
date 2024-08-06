# Exercise: Instantiate a custom Object
'''
This is your first experience creating classes and objects in Python. 
You will be following a sequential process where you will create a class, 
define its state by creating variables and functions to define its attributes and 
behavior, and then instantiate it using some variable. 
Finally, you will use the class members to get the desired output.
'''

# Define class MyFirstClass
class MyFirstClass:
    print('Who wrote this?')
    # Define string variable called index
    index = 'Author-Book'
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # variable + “ wrote the book: ” + variable
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()        
whodunnit.hand_list("Sun Tzu", "The Art of War")        


