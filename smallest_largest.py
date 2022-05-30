#  Write a program to accept 10 numbers from the user and display
#  the largest number.
i=1
a=0
while i<=10:
    num=int(input("enter number"))
    if a<num:
        a=num
    i=i+1
print(a,"is largest number")    