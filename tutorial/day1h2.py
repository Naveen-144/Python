#Calculate the average of N numbers entered by user.

n=int(input("Enter the range of array :"))
total=0
for i in range(n):
    num=int(input(f"Enter the number {i+1} :"))
    total=total+num
average=total/n
print(average)
