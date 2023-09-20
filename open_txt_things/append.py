file = open('myFile.txt', 'a')

for i in range(50,75,5):
    file.write("Number " + str(i) + "\n" )

