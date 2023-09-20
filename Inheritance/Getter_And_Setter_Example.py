class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    # this is not used anymore since we have the getter method below to do that:
    # self.email = fname + '.' + lname + '@blkb.ch'

    # below the property decorator: this is like the getter method in java
    # if someone changes the name of an employee it automatically changes the mail as well
    @property # if you access a property you can do it like an attribute WITHOUT () in the end
    def email(self):
        return 'E-Mail: {}.{}@blkb.ch'.format(self.fname, self.lname)
    @email.setter
    def email(self, mail):
        self.mail = mail

    def emp_output(self):
        return 'First Name: {} | Last Name: {} | E-Mail: {}'.format(self.fname, self.lname, self.email)

emp1 = Employee('John', 'Smith')
print(emp1.emp_output())

# if we now change the first name of emp1 we will not have a problem with the not updating email anymore
# because we created def email(self) which updates the mail through the fname and lname
emp1.fname = 'Aaron'
print("Employee with changed First Name and E-Mail: ")
print(emp1.emp_output())
emp1.email('manuel.buser@blkb.ch')



