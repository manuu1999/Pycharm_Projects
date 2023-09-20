class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = fname + '.' + lname + '@blkb.ch'
        # this is not used anymore since we have the
        # getter email method below to do that:

    # below the property decorator: this is like the getter method in java
    # if someone changes the name of an employee it automatically changes the mail as well
    @property # if you access a property you can do it like an attribute WITHOUT () in the end
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')
# we can now change the name of emp1 with our fullname setter method
emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# deletes emp1
del emp_1.fullname

