import statistics as S

in_file = open("Data.txt","r")

out_file = open("result.txt", "w")

line_num= 1

for line in in_file:
    line = line.strip("\n")
    line_list = line.split(";") # Erzeugt eine Liste aus der Zeichenkette
    int_list = []
    for element in line_list:
        int_list.append(int(element))

    line_mean = round(S.mean(int_list), 2)
    out_file.write("Mittelwert aus Zeile {0} = {1} \n".format(line_num, line_mean))
    line_num += 1

