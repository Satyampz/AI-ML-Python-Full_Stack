# f1= lambda a,b:a+b
# print(f1(5,7))


# test_marks=[1,2,3,4,5,6]

# grace_marks=list(map(lambda m:m*m , test_marks))

# print(grace_marks)

# max= reduce(lambda a,b:a if a>b else b , test_marks)

# print(max)
# def displayName():
    # print("Atul Sir")

# def My_decoration(fun):
#     def wrapperFun():
#         print("Good Morning")
#         print("*"* 10)
#         fun()
#         print("*"* 10)
#         print("Bye Bye ........")

#     return wrapperFun

# var=My_decoration(displayName)
# var()




def my_decorator3(fun):
    def wrapperfun(a,b,c):
        res=fun(a,b)
        res2=res+c
        return res2
    
    return wrapperfun

@my_decorator3
def addTwo(a,b):
    return a+b

addThree=my_decorator3(addTwo)
print(addTwo(10,20,30))