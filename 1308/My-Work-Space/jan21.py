# Inheritance
# Simple Inheritance

# class Parent(object):

#     def __init__(self,sn):
#         print("Parent Constructor is running")
#         self.surname=sn

#     def m1(self):
#         print(111)
    
# class Child(Parent):

#     def __init__(self,fn,sn):
#         super().__init__(sn)
#         print("Child Constructor is running")
#         self.firstname=fn

#     def m2(self):
#         # super().m1()
#         print(f"Student name is {self.firstname} {self.surname}" )

# c1=Child("Jay","Patil")
# # c1.m1()
# c1.m2()



# class Grand_Parent():

#     def __init__(self):
#         print("Grand Parent Constructor is running")

#     def m1(self):
#         print(111)


# class Parent(Grand_Parent):

#     def __init__(self):
#         super().__init__()
#         print("Parent Constructor is running")

#     def m2(self):
#         print(222)
    
# class Child(Parent):

#     def __init__(self):
#         super().__init__()
#         print("Child Constructor is running")

#     def m2(self):
#         super().m1()
#         super().m2()
#         print(333)

# c1=Child()
# # c1.m1()
# c1.m2()




# class Parent():

#     def __init__(self):
#         print("Parent Constructor is running")

#     def m1(self):
#         print(111)


# class Child1(Parent):

#     def __init__(self):
#         super().__init__()
#         print("Child1 Constructor is running")

#     def m2(self):
#         print(222)
    
# class Child2(Parent):

#     def __init__(self):
#         # super().__init__()
#         print("Child2 Constructor is running")

#     def m3(self):
#         super().m1()
#         print(333)

# c1=Child1()
# c2=Child2()
# # c1.m1()
# c1.m2()
# c2.m3()





class Parent1():

    def __init__(self):
        print("Parent1 Constructor is running")

    def m1(self):
        print(111)


class Parent2():

    def __init__(self):
        print("Parent2 Constructor is running")

    def m1(self):
        print(222)
    
class Child(Parent1,Parent2):

    def __init__(self):
        super().__init__()
        print("Child Constructor is running")

    def m3(self):
        super().m1()
        # super().m2()
        print(333)

c1=Child()

c1.m3()
print(c1.__mro__())