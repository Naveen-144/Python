# we use parenthesis for tuple()
#ordered, unchangable and allow duplicates

nd=('car','bike',5,8,'bike')
print(nd)
print(type(nd))
print(nd[-1])
print(nd[0])
print(nd[2:5])

for i in nd:
    print(i)

#trying to add value
#tuple.append("naveen")  so we can't change tuple

#we can change tuple as list
#we covert tuple to list then change tha element and again it converted to tuple
y=list(nd)
y[1]="naveen"
x=tuple(y)
print(x)
