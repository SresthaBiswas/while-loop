# Write a program to find the sum of following series:
# S = 1 + 4 – 9 + 16 – 25 + 36 – … … n terms
i=1
num=int(input("enter number"))
b=0
c=1
while i<=num:
    if i>1 and i%2==0:
        c=i**2
        print("+",c,end=" ")
    elif 1<i and i%2!=0:
        c=i**2*-1
        print(c,end=" ")
    else:
        print(i,end=" ")
    i=i+1