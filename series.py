# Write a program to add first n terms of the following series
# using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!
num=int(input("enter number"))
i=1
sum=0
a=1
while i<=num:
    print(a,"/",i,"!",end="+")
    i=i+1