# a=10
# b=20
# c=30
# print(a,b,c)
# print(a)
# print(b)
# print(c)

# print(a,b,c, sep="##")

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()

# def right_angle_triangle(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end=' ')
#         print()
# right_angle_triangle(5)

# def right_angle_triangle(n):
#     for i in range(n+1,1,-1):
#         for j in range(1,i):
#             print("*",end=' ')
#         print()
# right_angle_triangle(5)
# n=5
# for i in range(1,n+1):
#     print("* " * i)

# for i in range(n+1,1,-1):
#     print("* " * i)

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

# n=69
# for i in range(65,n+1):
#     for j in range(65,i+1):
#         print(chr(j),end=' ')
#     print()

n=5
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)

for i in range(n,0,-1):
    print((n-i)*" ","* "*i)