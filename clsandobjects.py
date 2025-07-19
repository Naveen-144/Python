#classes and objects

class Human:
    x=5  # x is the property and 5 is the value of the property

h1=Human() # Declaring the object
print(h1.x) 


class naveen:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #object methods
    def methods(self):
        print("hi my name is "+self.name)

h2=naveen("don",20)
#print(h2.name)
#print(h2.age)       

h3=naveen("nd",20)
h3.methods()
h2.methods()
h2.name="naveen"
h2.methods()