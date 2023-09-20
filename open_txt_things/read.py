file = open('myFile.txt', 'r')

for line in file:
    st = line.strip("\n")
    print(st)

