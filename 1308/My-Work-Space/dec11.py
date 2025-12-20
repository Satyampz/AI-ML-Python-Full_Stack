# s="123"

# for i in s:
#     print(i)

# s="Welcome to Kiran Academy"
# s= input("Enter a String :")
# char = input("Enter any char to find count = ")
# count=0
# for i in s:
#     if i == char:
#         count= count+1
# print (f"There are {count} {char}'s in {s}")

# # Infuilt functions 

# s="Facebook and Instagram"

# print(s.isupper())
# print(s.islower())

s="Satyam"

vowels="aeiouAEIOU"
count=0

for ch in s:
    if ch in vowels:
        count = count+1
print(count)