# variables only temporarily connected
num1 = 50
num2 = num1
num2 = 44
print(num1)
print(num2)
# list stay connected once
# you can connect them with li = li2
li = [50]
li2 = li
li2.append(40)
print(li)
print(li2)

