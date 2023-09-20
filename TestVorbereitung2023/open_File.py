try:
    with open("test.txt", "r") as file:
        myFile = file.readlines()
        print(myFile)
except Exception as e:
    print(e)

