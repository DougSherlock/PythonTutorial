import unittest
import datetime
import sys
import os
# print(sys.path)

from ..employee import Employee

print(f'__name__:{__name__}')
print(f'__package__:{__package__}')
print(f'__file__:{__file__}')


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # add the parent folder to the python path
# from employee import Employee


# print(sys.path)
# for p in sys.path:
#     print(p)
