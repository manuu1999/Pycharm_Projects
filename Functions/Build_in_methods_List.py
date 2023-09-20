li = ["Manuel",23,"Football"]
li.append("Basketball")
li2 = li
# because both lists are connected it removes also
# in li and not only in li2
li2.remove("Manuel")
print(li)
# makes a copy from the list
li3 = li2.copy()
# deletes all values from the list
li.clear()
print("After clear method: ", li, li2, li3)
# insert at specific place
li3.insert(0,25)
li3.insert(2, "Football")
print("After inserting: ", li3)
# count
print("The str value football was in li3: ", end="")
print(li3.count("Football"), "times")
# adds every char alone to a list / int is not allowed
li3.extend("hello")
print("After extend: ", li3)
# get the index of a value (first time found if its twice in your list)
print("Index of Value 'football' in your list: ", li3.index("Football"))
# remove last element from your list
li3.pop()
print("After pop method: ", li3)
# remove specific item from your list
# if value is twice in the list only first one gets removed
li3.remove("Football")
li3.remove(23)
print("After removing stuff: ", li3)

# reverse the order of your list:
li3.reverse()
print("After reversing: ", li3)
# sort the list (we remove all int otherwise it would get to complex)
li3.remove(25)
li3.sort()
print("After sorting: ", li3)
li3.sort(reverse=True)
print("Reverse Sorting: " ,li3)





