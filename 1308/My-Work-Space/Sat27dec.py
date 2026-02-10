# 27/12/2025
# l=[]
# print(bool(l))
# l=[10]
# print(bool(l))
# l=''
# print(bool(l))
# l='tp'
# print(bool(l))

#write a program to check whether a given number is a perfect number or not.
# num=int(input('enter number:'))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if sum==num:
#     print(f'{num} is perfect number')

# else:
#     print(f'{num} is not perfect number')


# def isperfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum+=i
#     if sum==num:
#         return True
#     else:
#         return False
    
# n1=isperfect(6)
# print(n1)

#write a program to check whether given number is armstrong number
# num=int(input('enter number:'))
# num_s=str(num)
# sum=0
# for i in num_s:
#     i=int(i)
#     sum+=i**(len(num_s))
# if sum==num:
#     print(f'{num} is armstrong number')
# else:
#     print(f'{num} is not armstrong number')

# def isarmstrong(num):
#     num_s=str(num)
#     sum=0
#     for i in num_s:
#         i=int(i)
#         sum+=i**(len(num_s))
#     if sum==num:
#         return True
#     else:
#         return False
# n1=isarmstrong(153)
# print(n1)

#next for loop

# for i in range(3):
#     for j in range(5):
#         print('*',end=' ')
#     print()

# for i in range(4):
#     for j in range(4):
#         print('*',end=' ')
#     print()

# def pattern(r,c):
#     for i in range(r):
#         for j in range(c):
#             print('*',end=' ')
#         print()

# pattern(10,5)

# for i in range(4):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()

# for i in range(1,4):
#     for j in range(1,5):
#         print(i,end=' ')
#     print()


# def pattern(r,c):
#     for i in range(1,r):
#         for j in range(1,c):
#             print(i,end=' ')
#         print()

# pattern(4,5)

# for i in range(3):
#     for char in 'ABCD':
#         print(char,end=' ')
#     print()

# print(ord('A'))
# print(chr(90))

# for i in range(3):
#     for j in range(ord('A'),ord('D')+1):
#         print(chr(j),end=' ')
#     print()

# for i in range(5):
#     for j in range(5,0,-1):
#         print(j,end=' ')
#     print()

# for i in range(5):
#     for j in range(ord('E'),ord('A')-1,-1):
#         print(chr(j),end=' ')

#     print()

# for i in range(5):
#     for j in range(5):
#         print(chr(ord('E')-j),end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# for i in range(5):
#     for j in range(0,i+1):
#         print(chr(ord('A')+j),end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# sp=5
# for i in range(1,6):
#     for k in range(0,(sp-i)):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# sp=5
# for i in range(1,6):
#     for k in range(0,sp-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(j,end=' ')s

#     print()

# sp=5
# for i in range(1,6):
#     for k in range(0,sp-i):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# practice
# 123
# 231
# 312

# write a program to calculate GCD