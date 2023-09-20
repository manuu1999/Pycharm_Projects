""" zeige folgende Telefonnummer
ohne Bindestriche """
number = "123-456-7890"

for i in number:
    if i == "-":
        continue
    print(i, end="")


