import unittest
import datetime


class Employee:

    total_emps_created = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@company.com'
        Employee.total_emps_created += 1

    def __del__(self):
        Employee.total_emps_created -= 1
        
    def __repr__(self) -> str: # unambiguous representation of an object - for developers
        return f'Employee({self.first} {self.last} {self.pay})'

    def __str__(self) -> str: # representation of an object - for users
        return f'{self.fullname()} {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    # property decorator - a method that behaves like an attribute
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        print('Delete Name!')
        self.first = None
        self.last = None

    @fullname.deleter
    def fullname(self):
        if self.fullname:
            first, last = self.fullname.split()
            self.first = first
            self.last = last

    @property # property decorator allows email function to be accessed using .email rather than .email()
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    def apply_raise(self):
        #[equivalent] self.pay = int(self.pay * Employee.raise_amt)
        self.pay = int(self.pay * self.raise_amt) # using 'self.raise_amt' permits instances and subclasses to override

    # decorator to define a class method
    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # constructor that is a class method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    # static method does not require instance or class
    @staticmethod
    def is_workday(day):
        if day.weekday() in (5, 6): # day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def get_emp_count(self) -> int:
        return len(self.employees)


emp1 = Developer('Doug', 'Sherlock', 100000, 'python')
emp2 = Developer('Bob', 'Smith', 1000, 'python')


# print(emp1.email)
# print(len(emp1))
# print(emp1 + emp2)
# print(repr(emp1))
# print(str(emp1))

# print(help(Developer))
# exec(open("test/test_employee.py").read())

class TestEmployee(unittest.TestCase):

    def test_fullname_setter(self):
        e1 = Employee('Doug', 'Sherlock', 100000)
        first = e1.first
        last = e1.last
        email = e1.email
        fullname = e1.fullname
        e1.fullname = fullname
        self.assertEqual(e1.first, first)
        self.assertEqual(e1.last, last)
        self.assertEqual(e1.email, email)
        self.assertEqual(e1.fullname, fullname)

    def test_manager(self):
        emp1 = Developer('Doug', 'Sherlock', 100000, 'python')
        mgr1 = Manager('Sue', 'Smith', 900, [emp1])
        self.assertEqual(mgr1.get_emp_count(), 1)
        emp2 = Developer('Test', 'User', 90000, 'java')
        mgr1.add_emp(emp2)
        self.assertEqual(mgr1.get_emp_count(), 2)
        mgr1.remove_emp(emp1)
        self.assertEqual(mgr1.get_emp_count(), 1)

    def test_raise_amt(self):
        emp = Employee('Doug', 'Sherlock', 100)
        dev = Developer('Test', 'User', 100, 'python')
        emp.apply_raise()
        dev.apply_raise()
        self.assertGreater(dev.pay, emp.pay)

    def test_developer(self):
        emp1 = Developer('Doug', 'Sherlock', 100000, 'python')
        emp2 = Developer('Test', 'User', 90000, 'java')
        self.assertEqual(Employee.total_emps_created, 2)
        self.assertEqual(emp1.prog_lang, 'python')
        self.assertEqual(emp2.prog_lang, 'java')

    def test_is_workday(self):
        self.assertFalse(Employee.is_workday(datetime.date(2021, 2, 7)))        
        self.assertTrue(Employee.is_workday(datetime.date(2021, 2, 8)))

    def test_from_string(self):
        pay = 90
        first = 'Jane'
        last = 'Winters'        
        emp = Employee.from_string(f'{first}-{last}-{pay}')
        self.assertEqual(emp.fullname(), f'{first} {last}')
        self.assertEqual(emp.pay, pay)

    def test_total_emps_created(self):
        emp1 = Employee('Doug', 'Sherlock', 100000)
        emp2 = Employee('Test', 'User', 90000)
        self.assertEqual(Employee.total_emps_created, 2)



if __name__ == '__main__':
    unittest.main()