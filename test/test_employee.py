import unittest
import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # add the parent folder to the python path
from employee import Employee
# from employee import Employee
# from ..employee import employee
# print(sys.path)

class TestEmployee(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()