# wap to print no.s fron 1 to `10` ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def m1():
#     for i in range(1,11):
#         print(i ,end=" " )
# m1()

# wap to print no.s fron 1 to 30 usnig step size 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def m2():
#     for i in range(1,30,3):
#         print(i ,end=" ")
# m2()


# wap to print no.s fron 10 to 1  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def m3():
#     for i in range(10,0,-1):
#         print(i ,end=" ")
# m3()

# wap to print no.s fron 1 to `10` ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a=1
# while a<=10:
#     print(a ,end=" ")
#     a=a+1

# wap to print no.s fron 1 to 30 usnig step size 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# b=1
# while b<=30:
#     print(b ,end=" ")
#     b=b+3

# wap to print no.s fron 10 to 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# c=10
# while c>=1:
#     print(c ,end=" ")
#     c=c-1

# wap to print a input and o/p range ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a=int(input("Enter a start point"))
# b=int(input("Enter a end point"))

# for i in range(a,b+1):
#     print(i ,end=" ")


# wap to print summation from 1 to 10 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)

#  same using while loop~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# i=1
# while i<=10:
#     sum=sum+1
# print(sum)

# using inpur function~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# a=int(input("Enter a start point : "))
# b=int(input("Enter a end point : "))

# sum=0
# for i in range(a,b+1):
#     sum=sum+i
# print(sum)
# i=1
# while i<=b:
#     sum+=i
# print(sum)

# sum=0
# for i in range(1,11):
#     if i%2 == 0:
#         sum=sum+i
# print(sum)


# program to calculate sum where numbers is completely divisible by 3 and 4
# l=[11,22,33,44,67,89,12,36,48,67]
# sum=0
# for i in l:
#     if i%3==0 and i%4==0:
#         sum=sum+i
# print(sum)


# write a prog to cal sum of total marks and percentage in a Dictonary

# marks={'math':78 ,'science':67 ,'history':90 ,'hindi':94 ,'marathi':85}
# sum=0
# for marks in marks.values():
#     sum=sum+marks
# print(sum)

# for mk in marks.values():
#     sum=sum+mk

# total=len(marks)*100
# per=(sum/total)*100
# print(per)


# write a prog to cal Discount and print dic again 


# product_mrp={'laptpo':60000 ,'TV':40000 ,'mobile':20000 }
# product_sp={}

# for product,mrp in product_mrp.items():
#     dp=mrp*15/100
#     sp=mrp-dp
#     # var[key]=values
#     product_sp[product]=sp
# print(product_mrp)
# print(product_sp)


# product_mrp={'laptpo':60000 ,'TV':40000 ,'mobile':20000 ,'laptop_bag':2000 ,'table':5000 }
# product_sp={}

# for product,mrp in product_mrp.items():
#     if mrp>=25000:

#         dp=mrp*20/100
#         sp=mrp-dp
#         # var[key]=values
#     else:
#         dp=mrp*10/100
#     sp=mrp-dp
#     # var[key]=values
#     product_sp[product]=sp
# print(product_mrp)
# print(product_sp)


# Write a prog to cal length of string without using inbuilt function 

# s="Dwarkadhish"
# cnt=0
# for i in s:
#     cnt=cnt+1
# print(cnt)

# Write a prog to cal num of vowels in a given string without using inbuilt function 

# s="Welcome to python world"
# s1="aeiouAEIOU"
# cnt=0
# for i in s:
#     if i in s1:
#         cnt=cnt+1
# print(cnt)

# Write a prog for reversing a string without using slicing


# s="instagram"
# rev=""
# for ch in s:
#     rev=ch+rev
# print(rev)

# WAP for chacek a palindrome

# s=input("Enter a String : ")
# rev=""
# for ch in s:
#     rev=ch+rev

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

