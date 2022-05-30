# Write a program to check whether a number is prime or not.
a=int(input("enter number"))
i=2
while i<a//2:
    if a%i==0:
        print(a,"is not a prime number")
        break
    i=i+1
else:
    print(a,"is prime number")