#functions
def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Hi')) #parameter pass

def hello_func2(greeting, name='you'):
    return '{},{}'.format(greeting, name)

print(hello_func2('Hi'))
print(hello_func2('Hi', 'abhipsha'))

def student_info(*args, **kwargs): #positional and keyword arguments
    print(args)
    print(kwargs)
    
student_info('Math','art', name='john', age = 22)
courses = ['maths', 'art']
info = {'name': 'John', 'age':22}
student_info(*courses, **info)

