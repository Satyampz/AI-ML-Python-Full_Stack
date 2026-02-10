# Simple Inheritance

class Parent:

    def __init__(self):
        print("Parent Constructor is running")

    def m1(self):
        print(111)
    
class Child(Parent):

    def m2(self):
        print(222)

# p1=Parent()
# p1.m1()

c1=Child()
# c1.m1()
c1.m2()