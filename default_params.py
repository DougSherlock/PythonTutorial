'''
When Python functions are called for the first time, their default parameters are initialized.
This can lead to unexpected behavior on subsequent calls.

reference:  https://www.youtube.com/watch?v=zdJEYhA2AZQ
'''

import time
from datetime import datetime

def display_time_bad(time=datetime.now()):
    print(time.strftime('%B %d, %Y %H:%M:%S'))


# same time is printed every time
display_time_bad()
time.sleep(1)
display_time_bad()
time.sleep(1)
display_time_bad()
time.sleep(1)


def display_time_good(time=None):
    if time is None:
        time=datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))


# same time is printed every time
display_time_good()
time.sleep(1)
display_time_good()
time.sleep(1)
display_time_good()
time.sleep(1)


def add_employee_bad(name, emp_list=[]):
    emp_list.append(name)
    print(emp_list)

# when emp_list parameter defaults to an empty list, it grows each time the fuction is called
add_employee_bad('Jim')
add_employee_bad('Ruth')


# when emp_list parameter defaults to 'None', it is initialized each time the fuction is called
def add_employee_good(name, emp_list=None):
    if emp_list is None:
        emp_list = []
        
    emp_list.append(name)
    print(emp_list)

add_employee_good('Jim')
add_employee_good('Ruth')
