#with open('text2.txt','w') as f: #if file already exists then it'll overwrite it
    #f.write('hello')
with open('text.txt','r') as rf:
    with open('text2.txt','w') as wf:
        for line in rf:
            wf.write(line)
            
#for picture use bytes , binary