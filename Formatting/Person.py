class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence4 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(end="Example with own class and class object: ")
print(sentence4)



