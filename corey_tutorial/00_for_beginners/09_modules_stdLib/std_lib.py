import random

courses = ['History', 'Math', 'Physics', 'CompSci']
random.shuffle(courses)
print(courses)
print()
random_courses = random.choice(courses)
print(random_courses)
print(courses)
print()


import math

rads = math.radians(90)
print(rads)
print(math.sin(rads))
print()


import datetime
import calendar

today = datetime.date.today()
print(today)
print(calendar.isleap(2019))
print(calendar.isleap(2020))
print()

import os

print(os.getcwd())


