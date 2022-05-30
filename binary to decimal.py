# Write a program to convert binary to decimal.
i=0
num=input("enter number")
c=0
while i<len(num):
    r=num[::-1]
    b=int(r[i])
    d=b*2**i
    c=c+d
    i=i+1
print(c)