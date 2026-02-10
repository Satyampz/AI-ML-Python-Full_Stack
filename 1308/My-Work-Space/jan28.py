# print(4/2)
# print(4/4)
# try:
#     print(4/3)
# except ZeroDivisionError as e:
#     print("Infinity")
#     print(e)

# print(4/1)
# print(4/3)
# print(4/5)

# try:
#     num1=int(input("Enter a number 1 :"))
#     num2=int(input("Enter a number 2 :"))
#     print(num1/num2)

# except Exception as e:
#     print("Write only decimal numbers...")
#     print(e)

# except (ZeroDivisionError,NameError,ValueError) as e:
#     print("Write only decimal numbers...")
#     print(e)

# print(4/2)
# print(4/4)
# try:
#     print(4/10)

# except ZeroDivisionError as e:
#     print("Infinity")
#     print(e)

# else:
#     print("Successfully Completed division")
    
# print(4/1)
# print(4/3)
# print(4/5)


print(4/2)
print(4/4)
try:
    print(4/0)

except ZeroDivisionError as e:
    print("Infinity")
    print(e)

else:
    print("Successfully Completed division")
    
finally:
    print("Clean up Activity")

print(4/3)
print(4/5)