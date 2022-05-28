i=1
while i<=4:
    j=1
    while j<=4-i+1:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1
    print()
    i=i+1
i=2
while i<=5:
    j=1
    while j<=i:
        print(" ",end="")
        j=j+1
    k=5
    while k>i:
        print("*",end=" ")
        k=k-1
    print()
    i=i+1