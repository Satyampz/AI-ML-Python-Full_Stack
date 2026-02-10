import re

# Matching pattern in string 

# s = "I love python programming"

# Match function
# search function
# findall function

# pattern = r"o"

# r1= re.match(pattern , s)

# print(r1)

# r2 = re.findall(pattern,s)

# print(r2)

# s = "I love Python programming"
# s1= "Amit got 88, 91 and 95 marks in his exams and tptal he got 550"
# s2= "Jay mobile number is 8798985236 and Amit's mobile number is 9887895624"
s3= "Jay email id is 123jay@gmail.com and amit's email id is amit@gmail.com"

pattern= r"\b[a-zA-Z]+@\w+\.\w+\b"

r=re.sub(pattern,"********@***.com",s3)

print(r)











# pattern = r"\d+"

# pattern = r"\b9\d*"

# pattern = r"\b[pP]\w{7,}

# pattern = r"\d{6}\b"

# r=re.findall(pattern,s2)

# r=re.sub(pattern,"xxxxxx",s2)

# print(r)

# sum=0

# for i in r:
#     sum += int(i)

# print("Total =",sum)