import random
li = []
for i in range(1,11):
    num = random.randint(1,500)
    li.append(num)

max_num = max(li)
print(li)
print(max_num)

