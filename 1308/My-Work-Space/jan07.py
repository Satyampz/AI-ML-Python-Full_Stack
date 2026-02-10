test_matks=[67,87,77,99,56,76]
# # grace_marks=[]

# def addfive(n1):
#     return n1+5
# # for i in test_matks:
# #     grace_marks.append(i+5)

# # for i in test_matks:
# #     m=addfive(i)
# #     grace_marks.append(m)

# # print(grace_marks)


# marks=list(map(addfive,test_matks))
# print(marks)

# topper_list=[]
# def topper(marks):
#     return marks>85

# topper_list=list(filter(topper,test_matks))
# print(topper_list)

from functools import reduce
# def addTwo(a,b):
#     return a+b

# sum=reduce(addTwo,test_matks)
# print(sum)

def my_max(a,b):
    if a>b:
        return a
    else:
        return b
max_num=reduce(my_max,test_matks)
print(max_num)