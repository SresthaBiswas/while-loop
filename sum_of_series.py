# Write a program to find the sum of following series:
# 1 + 2 + 6 + 24 + 120 . . . . . n terms
i=1
num=int(input("enter number"))
b=1
c=0
while i<=num:
    b=i*b
    c=b+c
    print(b)
    i=i+1
print(c,"total of the series")