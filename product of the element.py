# Write a program to find the sum of the digits of a number 
# accepted from the user.
a=int(input("enter number"))
i=10
while a>i:
    if a>=i and a<100:
        b=a//10
        c=a%10
        d=b*c
        print(d)
        i=i*a