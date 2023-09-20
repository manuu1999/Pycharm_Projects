# average

total = 0.0 # summe der eingaben
count = 0 # anzahl eingaben

value = float(input("ganze positive zahlen eingeben (or -1 to EXIT)"))

while value != -1:
    count += 1
    total += value
    print("aktuelle summe: ", total)
    value = float(input("ganze positive zahlen eingeben (or -1 to EXIT)"))

if count == 0:
        print("Keine Eingaben gemacht!")

else:
    mean = total / count
    print("Mittelwert der Eingaben: ", round(mean,2))