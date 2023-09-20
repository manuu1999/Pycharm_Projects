# always first the key and then the value for it (can also be a list)
student = {'name':'John', 'age': 23, 'courses':['Math','CompSi']}
print("1: ", student)
print("2: ", student.get('Name'))
# second variables defines what to return if not found
print("3: ", student.get('Phone', 'Not here'))
print("4: ", student['age'])

# add another key to the dictionary:
student['Matric. Num.'] = '234.231-234'
print("5: ", student)
# if it's already exists it overrides it
student['name'] = 'Steven'
print("6: ", student)
# updates smth or if it's not there it just adds
student.update({'name':'Herbert', 'age':55, 'phone': '78-4543-345'})
print("7: ", student)
# if you want to delete a key
del student['age']
print("8: ", student)
# or second option to remove a key
age = student.pop('courses')
print("9: ", student)
# get different info from our dictionary:
print("10: ", len(student))
print("11: ", student.keys())
print("12: ", student.values())
# keys and values together:
print("13: ", student.items())

# to loop through a dictionary we need this function - items()
for key,value in student.items():
    print("Loop: ",end="")
    print(key, value)







