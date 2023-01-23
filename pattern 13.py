n=int(input("enter n:"))
for x in range(1,n+1):
    for y in range(1,x+1):
        if y==1:
            print(y,end=" ")
        elif x==y:
            print(y,end=" ")
        elif x==n:
            print(y,end=" ")
        else:
             print(end="   ")
    print()
