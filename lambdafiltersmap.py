# lambda function = small and ananymous function
#any number of arguments but one expression
# syntax for this is lambda arguments: expression

def f1(x):
    return x+10

print(f1(5))

# in lambda function
a=lambda x:x+10
print(a(5))

# map function runs a function on all items in a collection

collec=[1,2,3,4,5]
collec2=[]
for x in collec:
    collec2.append(float(x))
print(collec2)    

#in map function
col=[1,2,3,4,5,6,7]
col2=list(map(float,col))
print(col2)

#doubling it
double=list(map(lambda x:x*2 , col))
print(double)

# filter function runs a function on all items in a colllection but only stores the true values

age=[12,14,15,13,16,17,56,34,75,34,87]
def adult(x):
    if x>=18:
        return True
    else:
        return False

adults=list(filter(adult,age))
print(adults)

ad=list(filter(lambda x:x>=18,age))
print(ad)