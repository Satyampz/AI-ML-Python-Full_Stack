# class Students:
#     # class variable
#     c_name="TKA"

#     def __init__(self,r,n,m):
#         self.roll=r
#         self.marks=m
#         self.name=n



# s1=Students(n="Jay",m=88,r=1)
# s2=Students(2,"Viru",88)

# print(s1.name)
# print(s1.c_name)

# s1.c_name="JBK"
# print(s2.c_name)

# print(Students.c_name)


class Students:
    # class variable
    c_name="TKA"

    def __init__(self,r,n,m):
        self.roll=r
        self.marks=m
        self.name=n

    def display(self):
        print(f"Student name is = {self.name}")
        print(f"Student roll no is = {self.roll}")
        print(f"Student marks is = {self.marks}")

s1=Students(1,"Jay",88)
s1.display( )
