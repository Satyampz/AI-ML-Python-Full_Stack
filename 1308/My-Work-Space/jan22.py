# # Polymorphism

# class Book:

#     def __init__(self,n,p):
#         self.title =n
#         self.price=p

#     def __add__(self,other):
#         return self.title + other.price



# b1= Book("Core Python ",250)
# b2= Book("Advance Python" , 450)

# # print(b1+b2)
# print(b1.__add__(b2))


class Parent:

    def Property(self):
        print("Flat, Home, car, Bank Balance, Gold")

    def marry(self):
        print("Girl A")

class Child(Parent):

    def Property1(self):
        print(" Bike, Balance ")

    def marry(self):
        super().marry()
        print("Girl B")

jay=Child()
jay.Property()
jay.Property1()
jay.marry()