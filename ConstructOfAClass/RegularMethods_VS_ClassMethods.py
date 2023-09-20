class Employee:
    raise_amount = 1.04 # class variable

    # a regular method already takes the instance as a first argument normally it's called self
    # if you want to change that you have to turn them into class methods - see below
    def __init__(self,fname,lname, pay):
        self.fname = fname # instance variable
        self.lname = lname # instance variable
        self.pay = pay # instance variable
    def emp_output(self):
        return 'First Name: {} | Last Name: {} | Salary: {}'.format(self.fname,self.lname,self.pay)

    @classmethod # automatically changes in all objects in the class not only in the instances
    # now we receive the class as a first argument instead of the instance
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    # Alternative Constructor to create employee object from String 'John-Doe-70000'
    @classmethod
    def from_String(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

emp1 = Employee("Manuel", "Buser", 50000)
emp2 = Employee("Andreea", "Butnarciuc", 60000)

print(emp1.raise_amount)
print(emp2.raise_amount)
Employee.set_raise_amount(1.08)
print(emp1.raise_amount) # now all object from Employee class have a new raise_amount
print(emp2.raise_amount)
emp1.set_raise_amount(1.12) # even if you run class method from an instance it changes it in all objects from the class
print(emp1.raise_amount)
print(emp2.raise_amount)

# creates Class Object with our new alternativ class method constructor
emp_str_1 = 'John-Doe-70000'
emp3 = Employee.from_String(emp_str_1)
print(emp3.emp_output())





