S=" Satyam Zope "

count=0

for ch in S:
    if ch == "a":
        count = count + 1
print(f"Total no. of a in {S} is", count )

print(S)

print(S[1:4]) 

print(S[4:7]) 

print(S[-8:-4]) 

print(S[-10:-4]) 

print(S[ :6])  

print(S[6: ]) 

print(S[ : : 2])

print(S[ : : -2])

print(S[ -1: : -2])

print(S[6:3:1])

print(S[6:3:-1])

print(S[ : :-1])

print(S[ : :-2])

for ch in S:
    if ch == " ":
        count = count + 1
print(f"Total no. of space in {S} is", count )

for ch in S:
    if ch == "am":
        count = count + 1
print(f"Total no. of am in {S} is", count )