class Student:

    #Constructor
    def __init__(self,r,n,c,s):
        self.roll=r
        self.name=n
        self.city=c
        self.sub=s

s1 = Student(2,"Pavan","Pune","Python")
print(f"Student name is {s1.name} and roll no. is {s1.roll}")

s2 = Student(3,"Shruti","Nashik","Java")
print(f"Student name is {s2.name} and roll no. is {s2.roll}")

# print(s1.city)