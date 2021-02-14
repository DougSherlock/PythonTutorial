import random
courses = ['History', 'Math', 'Physics']
course = random.choice(courses)
print(course)

import calendar
import datetime
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
print(os.getcwd())
print(os.__file__)