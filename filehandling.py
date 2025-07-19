#file handling
f=open("nd.txt" , "w") #opened the file in "w" (write) mode
f.write("navee the don")
f.close()

with open("nd.txt") as f: #using with open to auto close the file
    print(f.read())
    f.seek(0)  # move file cursor back to the beginning
    x= f.read()
    print(x)

with open("nd.txt","w") as f: # here we are over writing so the naveen don will erased
    f.writelines("you rock\n")
    f.writelines("you the best\n")

with open("nd.txt") as f:
    print(f.readline())
    print(f.readline())

with open("nd.txt") as f:
    for x in f:
        print(x)

with open("nd.txt" ,"a") as f: # here we adding new line without erasing existing line tjis is appending
    f.write("a new line")

with open("nd.txt", "r") as f:
    print(f.read())

# create new file
with open("new.txt","x") as n: # "x" is to create new file
    n.write("this is new file")

with open("new.txt","r") as n:
    print(n.read())

import os 
os.remove("new.txt")

if os.path.exists("nd.txt"):
    os.remove("nd.txt")
else:
    print("the file is not exist")