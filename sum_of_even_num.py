# Accept two numbers from the user and display sum of even 
# numbers between them(including both)
i=0
a=int(input("enter number"))
b=int(input("enter number"))
while a<=b:
    if a%2==0:
        i=i+a
    a=a+1
print(i,"is sum of even numbers")