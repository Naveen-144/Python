num=6
found=0
for i in range(2,num):
    if num%i==0:
        found=1
        break

if found==1:
    print("not a prime")

else:
    print("prime")


    