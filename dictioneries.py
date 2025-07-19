#unordered , changeble and do not allow duplicate
# use curly bracs and we store the data in the form of key and values

nd={"name":"naveen",
    "age":20,
    "DOB":"9-11-2004",  #here the name age are all are keys and the naven 20 are all valuse and we cannot duplicate
    "vehicle":"mustang",
    "fruits":["apple","orange"]  #we can also mention list
    }

print(nd)
print(len(nd))
print(type(nd))

#to access values in dictionery
x=nd["name"]
print(x)
print(nd["age"])
z=nd.get("fruits")
print(z)

#list comprehension
keys=["name","age","DOB"]
y=[nd[k]for k in keys]
print(y)

#changing values in dictionery
nd["vehicle"]="aston"
print(nd)

nd.update({"age":21})
print(nd)

nd["colour"]="Black"
print(nd)

#removing values
nd.pop("fruits")
print(nd)