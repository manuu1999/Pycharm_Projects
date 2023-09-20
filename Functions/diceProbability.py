import random
li = []
li2 = []
for i in range(1,101):
    val = random.randint(1,6)
    li.append(val)

li2.append(li.count(1))
li2.append(li.count(2))
li2.append(li.count(3))
li2.append(li.count(4))
li2.append(li.count(5))
li2.append(li.count(6))
print(li2)
# old way to do it
print("Number one came", li2[0], "times.")
# Smoother way to do it
print("Number two came {0[1]} times. ".format(li2))
print("Number three came {0[2]} times. ".format(li2))
print("Number four came {0[3]} times. ".format(li2))
print("Number five came {0[4]} times. ".format(li2))
print("Number six came {0[5]} times. ".format(li2))



