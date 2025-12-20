# Acceptstring from console and display its data typeon console

# a=input("Enter a String :")
# print(a)
# print(type(a))

# accept string from termnal and display and display its length on secreen

# a=input("Enter a String :")
# print(a)
# print("Lenghth of given string is ",len(a))

# wap to check a lenghth of given string if length is more than 8 then its a valid string either invalid

# a=input("Enter a String :")
# if len(a) >=8:
#     print("Valid string")
# else:
#     print("Invalid String")


# wap to check a lenghth of given string if length is more than 8 then its a valid string either invalid
#  if that string contains white spaces then aslo str is invalid

# a=input("Enter a String :")
# if len(a) >=8 and ' ' not in a:
#     print("Valid string")
# else:
#     print("Invalid String")

# if len(a) < 8 or ' ' in a:
#     print("Invalid string")
# else:
#     print("Valid String")

# using for loop HW

# wap to check a lenghth of given string 
# 1if length is more than 8 then its a valid string either invalid
# 2if that string contains white spaces then aslo str is invalid
# 3 if that str not contans degit still it is invalid.

# a=input("Enter a String :")
# if len(a) >=8 and ' ' not in a and any(ch.isdigit() for ch in a):
#     print("Valid string")
# else:
#     print("Invalid String")
# 

# hw for loop
# for ch in a:
#     if ch in "0123456789":



# wap to check a lenghth of given string 
# 1if length is more than 8 then its a valid string either invalid
# 2if that string contains white spaces then aslo str is invalid
# 3 if that str not contans degit still it is invalid.
# 4 at least on capital latter must be present

# a=input("Enter a String :")
# if len(a) >=8 and ' ' not in a and any(ch.isdigit() for ch in a) and any(ch.isupper() for ch in a):
#     print("Valid string")
# else:
#     print("Invalid String")

# wap to check a lenghth of given string 
# 1if length is more than 8 then its a valid string either invalid
# 2if that string contains white spaces then aslo str is invalid
# 3 if that str not contans digit still it is a invalid.
# 4 contain at least one capital latter must be present.
# 5 contains at one special symbol !@#$%^&*.

# a=input("Enter a String :")
# if len(a) >=8 and ' ' not in a and any(ch.isdigit() for ch in a) and any(ch.isupper() for ch in a) and any(ch in "!@#$%^&*~" for ch in a):
#     print("Valid string")
# else:
#     print("Invalid String")

# Code for validation
def Pass_Validation(password):
    password=input("Enter a Password : ")

    if len(password) < 8:
        return F"your password len is {len(password)} and required is greater than 7"

    elif " " in password :
        return "Remove White spaces in your password"
    
    elif not any(ch.isdigit() for ch in password):
        return "Add at least one digit in your password"

    elif not any(ch.isupper() for ch in password):
        return "Add at least one upper case alphabate in your password"

    elif not any(ch in "!@#$%^&*~" for ch in password):
        return "Add at least one special chacter in your password"

    else:
        return "Password is Valid"

Pass_Validation(password)