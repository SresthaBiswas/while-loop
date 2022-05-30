# Write a while loop statement to print the following series
# 105, 98, 91 ………7
num=int(input("enter number"))
i=1
while num>=i:
    if num%7==0:
        print(num,end=" ")
    num=num-1