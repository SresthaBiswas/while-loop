# Write a program to print the following series till n terms.
# 1 4 9 16 25 _ _ _ _ _ n terms
i=1
num=int(input("enter number"))
while i<=num:
    print(i**2,end=",")
    i=i+1