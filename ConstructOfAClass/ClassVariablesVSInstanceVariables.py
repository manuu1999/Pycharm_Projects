class Employee:
    #example of class variable:
    raise_amount = 1.04
    num_of_employees = 0

    # code below same as constructor method in Java
    def __init__(self,fname,lname,pay):
        # these are all instance varaibles - different for each employee
        # below in apply_raise I showed an example of a class variable which is the same for all employees
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.mail = fname + "." + lname + "@blkb.ch"
        # increments employee amount class variable every time employee object gets created
        Employee.num_of_employees += 1

    # code below same as ToString method in Java - both have to be in class body
    # BUT it does not have a unique name such as ToString in Java - you can name it however you want
    def emp_all(self):
        return 'First Name: {} | Last Name: {} | Salary: {} | Mail: {}'.format(self.fname,self.lname,self.pay,self.mail)
    # you could also only integrate specific things in this method such as only first and last name:
    def emp_fullName(self):
        return 'First Name: {} | Last Name: {}'.format(self.fname,self.lname)

    # Here my example of a class variable - attention never forget self in brackets
    def apply_raise(self):
        # raises all salaries 4% from the whole company if they had a good year
        self.pay = int(self.pay * Employee.raise_amount) # or self.raise_amount

# initialize the class object with its attributes outside the class body
emp1 = Employee("Manuel", "Buser", 50000)
emp2 = Employee("Andreea", "Butnarciuc", 60000)

print(emp1.emp_all())
print(emp1.emp_fullName())
emp1.apply_raise()
emp2.apply_raise()
print("New Salary after raise for Emp1: ", emp1.pay)
print("New Salary after raise for Emp1: ", emp2.pay)
print("Current number of Employees:", Employee.num_of_employees)




