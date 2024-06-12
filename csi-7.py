# For loops
nums = [1,2,3,4,5]
for num in nums:
    if num==3:
        print('Found!')
        break
    print(num)
    
for num in nums:
    if num==3:
        print('Found!')
        continue #continue printing the no. even after the condition meets
    print(num)
    
for i in range(10):
    print(i)
# to start from 1
for i in range(1,11):
    print(i)

#while loop
while x < 10:
    print(x)
    x += 1