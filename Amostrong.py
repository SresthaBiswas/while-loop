# Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is
# equal to the sum of cubes of its digits, for example : 153 = 1^3 + 5^3 + 3^3.)
i=0
num=input("enter number")
l=len(num)
c=0
while i<l:
    b=int(num[i])**l
    c=c+b
    if num==c:
        break
    i=i+1
print(num,"is armstrong number")