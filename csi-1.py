#strings
message = "Dobby's World"
print(message)
print(len(message))
print(message[0])
print(message[0:7])#7 because 7 will not be included so to print till s we need to include 7th
print(message[7:])#slicing- includes space also
print(message.lower())
print(message.upper())
print(message.count('b'))
print(message.find('World'))
message2 = 'Hello World'
message2 = message2.replace('World','Universe')
print(message2)
message3 = message + ' : ' + message2
print(message3)
#instead of + , use formatted strings
message4 = '{}, {}. Welcome!'.format(message,message2)
print(message4)
#F string
message5 = f'{message}, {message2}. welcome!'
print(message5)
print(dir(message))
#print(help(str))#tells us every methods available for string
print(help(str.lower))#helps to get info about that particular function

