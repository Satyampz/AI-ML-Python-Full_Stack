# import json

# data={
#     "name":"Jay Patil",
#     "age": 20,
#     "city" : "pune",
#     "is_student": True,
#     "hobbies":["reading", "traveling", "coding"],
# }

# print(type(data))

# json_data = json.dumps(data,indent=4)
# print(type(json_data))

# print(data)
# print("--------------------------------------------------------------")
# print(json_data)




json_data={
    "name":"Jay Patil",
    "age": 20,
    "city" : "pune",
    "is_student": True,
    "hobbies":["reading", "traveling", "coding"],
}

with open('data.json','a')as file:
    json.dump(data,file, indent=4)