# This function should return n!
def factorial(n):
    if n == 0:
       return 1
    if n < 1:
        return None 
    return factorial(n-1)*n
