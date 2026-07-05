# #recursion
# def factorial(n):
# #     if (n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
    
# print(factorial(4))
# print(factorial(5))
# print(factorial(6))
# print(factorial(7))

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)
    
        
print(fact(3))
print(fact(4))
print(fact(6))
print(fact(7))

def series(n):
    if n==0:
        return 0
    else:
        return n + series(n-1)
    
print(series(5))
print(series(2))
print(series(10))


