# incremental approach of solving problem

def find_factorial_loop(n):
    if n < 0:
        return 0
    
    factorial = 1
    
    for i in range(1, n + 1):
        factorial = factorial * i
    
    return factorial
    
print(find_factorial_loop(5))

# Recursive approach of solving the problem

def find_factorial_recursion(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    else:
        return  n * find_factorial_recursion(n-1)

print(find_factorial_recursion(6))