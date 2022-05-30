a=int(input("enter number"))
i=0
while i<=a:
    b=a
    while b>=i:
        if b==i:
            print("*",end=" ")
        else:
            print(" ",end="")
        b=b-1
    c=1
    while c<=i:
        if c==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    i=i+1
z=1
while z<=a:
    c=0
    while c<=z:
        if c==z:
            print("*",end=" ")
        else:
            print(" ",end="")
        c=c+1
    b=a-1
    while b>=z:
        if b==z:
            print("*",end="")
        else:
            print(" ",end=" ")
        b=b-1
    print()
    z=z+1