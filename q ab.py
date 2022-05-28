a=int(input("enter"))
i=1
c=0
while i<=a:
    j=a
    while j>=i:
        print(" ",end="")
        j=j-1
    k=1
    c=c+1
    while k<=i:
        print(c,end=" ")
        k=k+1
    print()
    i=i+2
