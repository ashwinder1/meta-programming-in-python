# 1. Class definition of A     
class A:
   def __init__(self, c): # 1.1 Constructor for A
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self): # 1.2 Definition of local method alpha()
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)            # 2. Instantiating object 'a' over class A 
print(a.alpha())    # 3. Calling method alpha() over object of class A 

# 4. Class definition of B 
class B:
   def __init__(self, a):   # 5. Constructor for B 
       print("---------Inside class B----------")
       self.a = a


   print(a.alpha())     # 5.1 Calling method alpha() over object of class A
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)                # 5.2 Instantiating object a over class B *. 
print(a)


# statements inside a class body get executed irrespective of the instance creation

# namespace and scope of the variable is determined by the 
# interpreter before you create any instance of the class or call any function inside it.
