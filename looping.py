#for variable in sequence: this is the syntax

for i in range(5):
    print(i)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


#while condition:
count = 0
while count <=5:
    print(count)
    count += 1

#loop control statements
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

#nested loops

for i in range(3):
    for j in range(2):
        print(i, j)

for i in range(10):
    i+=2
    print(i)

#range(start, stop, step)    
for i in range(0,10,2):
    print(i)