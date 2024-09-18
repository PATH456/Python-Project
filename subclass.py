class Employee:
    company_name = "International Tech corp"
    raise_amount = 1.04

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, age, pro_lang):
        super().__init__(first, last, age)
        self.pro_lang = pro_lang

class Manager(Employee):

     def __init__(self, first, last, age, emp_supervise = None):
         super().__init__(first, last, age)
         if emp_supervise is None:
             self.emp_supervise = []
         else:
             self.emp_supervise = emp_supervise

     def add_emp(self, emp):
         if emp not in self.emp_supervise:
             self.emp_supervise.append(emp)

     def remove_emp(self, emp):
         if emp in self.emp_supervise:
             self.emp_supervise.remove(emp)

     def print_emp(self):
         for i in self.emp_supervise:
             print("==>", i.fullname())


emp1 = Developer("John", "Smith", 20, "Python")
emp2 = Developer("Tony", "Stark", 36, "Java")
manager1 = Manager("Peter", "Toddler", 45, [emp1])


manager1.add_emp(emp2)
manager1.print_emp()



























































































    






















