# Write a program to accept 10 numbers from the user and
#  display it’s average.
i=1
b=0
while i<=10:
    num=int(input("enter number"))
    b=num+b
    if i==10:
        _avrg=b/i
        break
    i=i+1
print(b,"is total")
print(_avrg,"is average of total")