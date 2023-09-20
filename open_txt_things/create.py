file2 = open("myFile.txt", "r")

file = open("create_File.txt", "x")

for line in file2:
    st = line.strip("\n")
    file.write(st)



