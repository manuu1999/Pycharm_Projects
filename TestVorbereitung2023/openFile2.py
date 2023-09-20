f = open("test.txt", "r")

contents = f.read()
file_as_list = contents.split("\n")
li = []
for i in file_as_list:
    i = i.split(" ")
    print(i)
    li.append(i)






