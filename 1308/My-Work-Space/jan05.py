# def sign_up(en,age,sal,cn):
#     print(f"Name of employee is : {en}")
#     print(f"Age of employee is : {age}")
#     print(f"Salary of employee is : {sal}")
#     print(f"Company name of employee is : {cn}")
# sign_up("Jay",24,25000,"Tcs")

def submit(**kwargs):
    print(kwargs)
    print(kwargs)

    for k,v in kwargs.items():
        print(k,"----->",v)

submit(name= "Pawan",mobile=7418529632)