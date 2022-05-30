# 20. Write a program to check whether a number is palindrome or not.
num=input("enter number")
i=0
b=""
while i<len(num):
    b=num[i]+b
    i=i+1
if int(num)==int(b):
    print(num,"is palindrome number")
else:
    print(num,"is not a palindrome number")