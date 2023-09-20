values = [0,0,0,0]
#Aufgabe A
for k in range(1,4):
    values.insert(k,k)
    values.pop(k+1)

print(values)
# Aufgabe C
for k in range(0,4):
    values.insert(k, k+1)
    values.pop(k+1)
# Aufgabe B
for i in range(len(values)):
    print(values[i])

# Aufgabe D
amount = 0
for i in range(len(values)):
    amount += values[i]
print(amount)
