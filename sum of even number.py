# Write a program to print the sum of the first 10 Even numbers.
num = int(input("enter number"))
i=1
sum=0
while i<=num:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)