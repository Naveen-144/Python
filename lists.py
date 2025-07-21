#it is used to store multiple items in a single variable.
#it is in square brac
#list are orderd changable and duplicate


n=['naveen',144,'don',314,True]
print(n)

print(len(n))  #length of the list

print(type(n)) #type of the list

print(n[0])
print(n[2:5])
print(n[2:])

for items in n:
    print(items)

n[1]=414 #altering the list
print(n)
n[1:3]=[144,'Dj']
print(n)

#inserting element
n.insert(5,'don') 
print(n)
n.insert(1,410) # now the 410 is index 1 and 144 is shit to inex 2
print(n)

#add to list
n.append("you rock") #it will add after don
print(n)

n.remove("you rock")
print(n)