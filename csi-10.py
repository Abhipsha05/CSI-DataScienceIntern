#File Objects
#f = open('text.txt', 'r')
#print(f.name)
#print(f.read)
#f.close()
with open('text.txt', 'r') as f:
    #f_contents = f.read() , you can also pass argument like read(100)
    #print(f_contents)
    #f_contents2 = f.readlines()
    #print(f_contents2)
    
    #for line in f:
        #print(line, end = '')
        
    size_to_read = 5
    f_contents = f.read(size_to_read)#reads 5 letters,spaces etc
    
    while len(f_contents)>0:
        print(f_contents, end='$')
        f_contents = f.read(size_to_read)
#f.seek(0) - start again to the beginning of the file
f.close()

