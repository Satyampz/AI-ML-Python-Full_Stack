try:

    fd =open("db.txt", "r")
    print("File openned in read mode.....")

    # for i fd:
    #     print(i)

    # data = fd.read(10)
    # data[1:5]
    data = fd.readline()
    # print(data[1:5])
    for i in data:
        print(i)


except FileNotFoundError as e:
    print("Pls check file name or path......")
    print(e)

finally:
    fd.close()