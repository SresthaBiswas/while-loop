# 16. Write a program to print the factorial of a number accepted by the user.
i=1
num=int(input("enter number"))
a=1
while i<=num:
    a=a*i
    print(a,end=" ")
    i=i+1