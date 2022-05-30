# Write a Python program to find those numbers which are
#  divisible by 7 and multiple of 5, between 1500 and
# 2700 (both included).
a=1500
b=2700
while a<=b:
    if a%5==0 and a%7==0:
        print(a,"is divisible by 7 and 5")
    a=a+1
