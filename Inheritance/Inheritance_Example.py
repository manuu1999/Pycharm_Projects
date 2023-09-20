class Employee:
    raise_amount = 1.04  # class variable
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def emp_output(self):
        return 'First Name: {} | Last Name: {} | Salary: {}'.format(self.fname, self.lname, self.salary)
    def apply_raise(self):
        # raises all salaries 4% from the whole company if they had a good year
        self.salary = int(self.pay * Employee.raise_amount) # or self.raise_amount


class Developer(Employee):
    raise_amount = 1.10 # new class variable - overwrites inherited one

    # how to add new attribute for subclass - inherit with super and add new ones
    def __init__(self, fname, lname, salary, prog_lang):
        super().__init__(fname, lname, salary) # pass to employee init method, so it can deal there with it
        self.prog_lang = prog_lang

    def dev_output(self):
        return 'First Name: {} | Last Name: {} | Salary: {} | Prog. Lang: {}'.format(self.fname,self.lname,self.salary,self.prog_lang)
                # \ this one is only putting code on the next line so the row is not too long

dev1 = Developer("Corey", "Schaefer", 50000, "PYTHON")
dev2 = Developer("Aron", "Shore", 70000, "JAVA")
print(dev1.dev_output())
print(dev2.dev_output())



