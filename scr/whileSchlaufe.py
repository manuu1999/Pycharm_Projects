# example of a while loop

# program checks if the values are already in the array

values = [4,2,5,1,8]
print("Aktuelle Werte:", values)

new_value = int(input("Neuen Wert eingeben: "))

while new_value in values:
    print("Dieser Wert ist schon vorhanden. ")
    print("Aktueller Werte: ", values)
    new_value = int(input("Neuen Wert eingeben: "))

# append function is to add a new value to an array
values.append(new_value)
print("Aktuelle Werte: ", values)

# this would be another possibility to print out
# the values from an array with is indexes
# it is a mix between for loop and for each loop from Java
for i in range(len(values)):
    print(i, values[i])
