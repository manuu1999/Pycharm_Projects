# Formatting option 1
person = {'name':'Jenn', 'age':23}
sentence1 = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print('Sentence 1: ', sentence1)

# you can use values also twice
tag = 'H1'
text = 'This is a headline'
sentence2 = '<{0}>{1}</{0}'.format(tag,text)
print('Sentence 2: ',sentence2)

# you can retrieve with the placeholder values from a list
li = ['Manuel', 23, "Fussball"]
sentence3 = 'Hello my name is {0[0]} and I am {0[1]} years old'.format(li)
print('Sentence 3: ',sentence3)

# access directly with keywords
sentence5 = 'My name is {name} and I am {age} years old.'.format(name='Jenn',age='30')
print('Sentence 5: ',sentence5)

