#Print numbers from 1 to 10.
for i in range(1,11,1):
    print(i)

#Print even numbers from 2 to 20.
for i in range(2,21,2):
    print(i)

#Print the multiplication table of a given number (e.g., 5).
for i in range(1, 11):
    print(f"{i} * 5 = {i * 5}")

#Calculate the sum of numbers from 1 to 100.
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

#print(sum(range(1, 101)))

#Print characters of a string one by one using a loop.
a="naveen"
for a in a:
    print(a)

#Print the first 10 square numbers (1², 2², ..., 10²).
for i in range(1,11):
    print(f"{i}^2 = {i*i}")

#Print only vowels from a string
d = "naveen"
for ch in d:
    if ch in {"a", "e", "i", "o", "u"}:
        print(ch)

#Use a while loop to find the factorial of a number.
i=1
fact=1
while i<=5:
    fact=fact*i
    i+=1
print(fact)
