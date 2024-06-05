#dictionary
student={
    'name': 'john',
    'age' : 25,
    'courses' :['maths', 'cs']
}
print(student['courses'])
print(student.get(('courses')))
print(student.get('phone','not found'))#phone key is not present in the dictionary hence it will print the default value
student['phone']='2345678910'
student['name']= 'Jane'
print(student)
student.update({'name': 'Janet', 'phone': 55555555, })
print(student)
#del student['age']
#age = student.pop('age')
print(student.items())
for key,value in student.items():
    print(key,value)
new_course = 'biology'
student['courses'].append(new_course)
print(student)