val1, val2, val3 = 1,2,3
on = True

if val1 < val2:
    print("Grün")
    if val2<val3:
        print("Gelb")
    else:
        print("Blau")
else:
    if on:
        print("Rot")
    else:
        print("Orange")
print("Schwarz")