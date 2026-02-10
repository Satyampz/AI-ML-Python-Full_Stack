# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# num = int(input("Enter number: "))
# print(f"Factorial of number {num} is:", factorial(num))

# def factorial(n):
#     print(f"Computing factorial of {n}! ")
#     if n == 1:
#         return 1

#     return n*factorial(n-1)
# print(factorial(5))

# def outerfun(x):
#     print(x)

#     def innerfun():
#         print("This is inner function")
#         print(x)
    
#     print("Calling inner function")
#     innerfun()

# outerfun(10)

def outerfun(a):
    def innerfun(b):
        return (a+b)
    return innerfun
addtwo=outerfun(10)

res=addtwo(5)

print(res)