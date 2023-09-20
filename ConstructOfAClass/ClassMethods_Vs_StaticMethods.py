class Employee:
    raise_amount = 1.04 # class variable
    ####################### Regular Methods (self) #################################################
    def __init__(self,fname,lname, pay):
        self.fname = fname # instance variable
        self.lname = lname # instance variable
        self.pay = pay # instance variable
    def emp_output(self):
        return 'First Name: {} | Last Name: {} | Salary: {}'.format(self.fname,self.lname,self.pay)

    def apply_raise(self):
        # raises all salaries 4% from the whole company if they had a good year
        self.pay = int(self.pay * Employee.raise_amount) # or self.raise_amount

    ####################### class methods (cls) ###################################################
    @classmethod # automatically changes in all objects in the class not only in the instances
    # now we receive the class as a first argument instead of the instance
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    ####################### static methods () ###################################################
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return  False # in python dates have this weekday method
        else:             # Monday is equal to 0 and Sunday equal to 6, etc.
            return True

emp1 = Employee("Manuel", "Buser", 50000)
print(emp1.emp_output())
emp1.set_raise_amount(1.12) # class method (cls)
emp1.apply_raise() # regular method (self)
print(emp1.emp_output())

import datetime # to check if our static method is working
my_date = datetime.date(2023,1,17)
print(Employee.is_workday(my_date)) # static method ()



