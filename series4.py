# Write a program to find the sum of following series
# 1 + 8 + 27 …………n terms
i=1
num=int(input("enter number"))
while i<=num:
    print(i**3,end=",")
    i=i+1