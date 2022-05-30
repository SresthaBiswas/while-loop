# Write a program to print first 10 integers and their squares like
# 1 1
# 2 4
# 3 9
# ………………...and so on
num = int(input("enter number"))
i=1
while i<=num:
    print(i,i**2)
    i=i+1