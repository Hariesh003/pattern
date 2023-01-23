n=int(input("enter n:"))
for x in range(n,0,-1):
    for y in range(x,n+1):
        if x%2!=0:
            print("1",end=" ")
        elif x==n:
            print("1",end=" ")
        elif y%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
         
