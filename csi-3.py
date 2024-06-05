#list
courses = ['History','maths','english', 'cs']
print(courses[0])
print(courses[0:2])#will print only 0 and 1
print(courses[2:])
courses.append('art')
print(courses)
courses.insert(0,'art')
print(courses)
courses_2 = ['science','eco']
#courses.insert(0,courses_2)
#print(courses)
courses.extend(courses_2)
print(courses)
courses.remove('art')
print(courses)
popped = courses.pop()
print(popped)
courses.reverse()
print(courses)
courses.sort()
print(courses)
nums = [9,6,56,1,3]
nums.sort(reverse=True)#for decending order
print(nums)
sorted_nums = sorted(nums)#sorting and storing without altering the original lists
print(sorted_nums)
print(min(nums))
print(sum(nums))

#finding values
print(courses.index('maths'))
#print(courses.index('eco'))
print('eco' in courses)
for item in courses:
    print(item)
    
for index, course in enumerate(courses):
    print(index, course)
for index, course in enumerate(courses, start = 1):
    print(index, course)
    
course_str = '-'.join(courses)#list values to string by joining
print(course_str)