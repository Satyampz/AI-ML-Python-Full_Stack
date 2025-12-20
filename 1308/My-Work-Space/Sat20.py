# n=5
# for i in range(0,n):
#     if n>1:
#         if n % i==0:
#             break
# else:
#     print("Prime Number")

# 1) WAP to take a no. and calculate the sum of its digit using a Loop.

# num=int(input("Enter a number ="))
# s=0
# while num > 0:
#     s+=num%10
#     num//=10    
# print("Sum of Digits :",s)

# 2)WAP to check if a given str is a palindrome or not, using loops.

# s=input("Enter a String : ")
# rev=""
# for ch in s:
#     rev=ch+rev
# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 3)WAP to check if a given str is a palindrome or not,without using loops.

# s=input("Enter a String : ")
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 4) WAP to find the frequency of each char in a str (how many times each char occurs) print in a dict formate

# s = input("Enter string: ")
# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)

# 5) WAP to check given no is prime or not

# num = int(input("Enter number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")

# 6) WAP to Print all Prime numbers between 1 and N also find cont in that range

# n = int(input("Enter N: "))
# primes = []
# cnt=0
# for num in range(2, n+1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)
#         cnt+=1
# print(primes)
# print("Total no.s in that range :",cnt)

# 7) Write a program to check whether a given number is a Perfect Number or not. # (Perfect number = sum of divisors = number, e.g. 6, 28)

# num = int(input("Enter number: "))
# s = 0

# for i in range(1, num):
#     if num % i == 0:
#         s += i

# if s == num:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")

# 8) Write a program to find all Perfect Numbers between 1 and 1000.

# perfect = []

# for num in range(1, 1001):
#     s = 0
#     for i in range(1, num):
#         if num % i == 0:
#             s += i
#     if s == num:
#         perfect.append(num)

# print(perfect)

# 9) Write a program to check whether a given number is an Armstrong Number or n #(Armstrong = sum of each digit^number of digits = original number, e.g. 153)

# num = int(input("Enter number: "))
# temp = num
# p= len(str(num))
# s = 0

# while temp > 0:
#     d = temp % 10
#     s += d ** p
#     temp //= 10

# if s == num:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

# 10) Write a program to print all Armstrong Numbers between 1 and 1000 and show total cnt.

# armstrong = []
# cnt=0
# for num in range(1, 1001):
#     temp = num
#     p = len(str(num))
#     s = 0

#     while temp > 0:
#         d = temp % 10
#         s += d ** p
#         temp //= 10

#     if s == num:
#         armstrong.append(num)
#         cnt+=1

# print(armstrong)
# print("Total Armstrong No.s upto 1000 :",cnt)

# 11) Write a orogram to find the factorial of a given number using a loop.

# num = int(input("Enter number: "))
# fact = 1

# for i in range(1, num+1):
#     fact *= i

# print("Factorial:", fact)


# 12) write a progras to calculata the sum of factorials of digits of #Example: 145 -> 1! 4! 51 =145  (special mumber check)

# num = int(input("Enter number: "))
# temp = num
# sum_fact = 0

# while temp > 0:
#     digit = temp % 10
#     fact = 1

#     for i in range(1, digit + 1):
#         fact *= i

#     sum_fact += fact
#     temp //= 10

# if sum_fact == num:
#     print("Special Number")
# else:
#     print("Not a Special Number")

# 13) write a program to Check given number is palindrome using for loop

# num = int(input("Enter number: "))
# s = str(num)
# rev = ""

# for i in s:
#     rev = i + rev

# if s == rev:
#     print("Palindrome Number")
# else:
#     print("Not Palindrome Number")
