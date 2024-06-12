import sys
import datetime
import calendar
import os
#import random
sys.path.append('A:\coding\python\csimodule.py')
import csimodule as cm
courses = ['maths','art','cs']
#index = csimodule.find_index(courses,'art')
index = cm.find_index(courses,'art')
print(index)

print(sys.path)
# 
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))
print(os.getcwd())