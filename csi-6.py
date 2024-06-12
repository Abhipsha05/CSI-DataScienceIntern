#conditions
language = 'Java'
if language == 'Python':
    print("python it is")
elif language == 'Java':
    print("Java it is")
elif language == 'C':
    print("C it is")
else:
    print('no match')
#boolean : and, or, not

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print('Admin Page')
elif not logged_in:
    print('Please log in')
else:
    print('Wrong creds')
    
a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)#compares location
print(id(a))
print(id(b))
#instead do:
c=a
print(a is c)#same id
condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition1 = 0
if condition1:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition1_1 = 25 #any random no.
if condition1_1:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition2 = []
if condition2:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition3 = {}
if condition3:
    print('Evaluated to True')
else:
    print('Evaluated to False')
condition4 = ''#empty string, not even space
if condition4:
    print('Evaluated to True')
else:
    print('Evaluated to False')