# std_db={1:"Jay" , 2:"Pavan" }

# for i,j in std_db.items():
#     print(i)
#     print(j)

movies2025={}
d_cast=["Ranbir Singh" , "Akshay Khanna" , "Sanjay Dutt" , "Sara Arjun"]
pushpa2_cast=["Allu Arjun" , "Rashmika Mandana" , "Sham Arjun"]
Chava_cast=["Akshay Khanna" , "Rashmika Mandana" , "Ayush Khan"]
Sam_cast=["Karin Dharma" , "Ram Sham" , "Saiyan khan"]

movies2025["Dhurandhar"]=d_cast
movies2025["Pushpa2"]=pushpa2_cast
movies2025["Chava"]=Chava_cast
movies2025["Sam"]=Sam_cast

# print(movies2025)

# print(movies2025.keys())

# for names in movies2025.keys():
#     print(names)

# for i,j in movies2025.items():
#     print(i, "total Cast:", len(j))


# cnt=0
# for name,cast in movies2025.items():
#     if "Akshay Khanna" in cast:
#         print("Movie with Akshay Khanna :", name)
#         cnt+=1

# print("Total Movies with Akshay Khanna :",cnt)

cnt=0
for name in movies2025:
    if "Akshay Khanna" in movies2025[name]:
        print("Movie with Akshay Khanna :", name)
        cnt+=1

print("Total Movies with Akshay Khanna :",cnt)