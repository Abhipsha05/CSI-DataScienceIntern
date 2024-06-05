#in list, they are mmutable i.e
list1 = ['hi','abcx']
list2 = list1
print(list1)
print(list2)
list1[0] = 'hello'
print(list1)
print(list2)#the value in list 2 also changes
#hence, we can use tuples
tuple1 = ('hi', 'abcx')
tuple2=tuple1
#tuple1[0] = 'hello'#We can't append or do much methods
print(tuple1)
print(tuple2)
#sets used to remove duplicate
courses={'art','maths','science', 'art', 'cs'}
print(courses)
cs_courses = {'cs','maths','compiler'}
print(cs_courses.intersection(courses))
print(cs_courses.difference(courses))
#empty list
empty_list = []
empty_list = list()
#empty tuple
empty_tuple = []
empty_tuple = tuple()
#empty set
empty_set = set()
#empty_set = {} : this will create an empty dictionary