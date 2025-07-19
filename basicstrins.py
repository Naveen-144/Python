# strings can be declare with double quotes as well as single quotes
name="naveen"
school='montfort'

print(name,school)

# multiline strings

about=""" naveen 
is a 
good boy"""

x='''this 
will also 
work in single 
quotes'''

print(about)
print(x)

# sring in python is basically a array

print(name[0])
print(len(name))

print("na" in name)
#slice the spice
print(name[2:5])
print(name[-5:-2])

print(name.upper()) #changes to upper case
print(name.lower()) #changes to lower case

a="hello, world   "
print(a.strip()) #this is to remove white spaces
print(a.replace("h","y")) # we can replace
print(a.split(",")) #we can split a string

d="don" 

print(name+" "+d)
b=d[::-1]
print(b)