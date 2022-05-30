# Write a program to display sum of odd numbers and even numbers separately that fall between two
# numbers accepted from the user.(including both numbers) 100 and 500.
i=int(input("enter number"))
num=int(input("enter number"))
sum=0
sum1=0
while i<=num:
    if i%2==0:
        sum=sum+i
    elif i%2!=0:
        sum1=sum1+i
    i=i+1
print("sum of even number",sum)
print("sum of odd number",sum1)