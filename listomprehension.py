# offer you smaller line of odes to reate new list from existing list

fruits=["apple","banana","mango","pineapples","kiwi"]
newfruits=[]

#general way
for x in fruits:
    if "i" in x:
        newfruits.append(x)

print(newfruits)

#list comprehension method
newfruits=[x for x in fruits if "a" in x]
print(newfruits)

nd=[x for x in fruits]
print(nd)

dn=[x for x in range(10) if x<6]
print(dn)

newfruits=[x if x!="banana" else "orange" for x in fruits]
print(newfruits)