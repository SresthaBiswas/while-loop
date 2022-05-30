# Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms
num=input("enter number")
i=1
t_m=int(input("enter number"))
while i<t_m:
    a=num*i
    print(a)
    i=i+1