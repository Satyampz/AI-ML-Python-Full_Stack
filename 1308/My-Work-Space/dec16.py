# r= range(5)
# print(type(r))
# print(r)
# l=list(r)
# print(l)

# for i in r:
#     print(i)

# r1= range(50,61)
# for i in r1:
#     print(i)

# r2= range(2,20,2)
# for i in r2:
#     print(i)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

# num=eval(input("Emter a numbar: "))
# for i in range(1,11):
#     # print(num,"*",i,"=", num*i)
#     print(f"{num} * {i} = {num*i}")

# print("{} * {} = {}".format(num,i,num*i))

s="Instagram"

for i in range(0, len(s)):
    if i%2 == 1:
        print(i, " ------> ", s[i])