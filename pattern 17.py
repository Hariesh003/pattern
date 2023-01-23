n=int(input("enter n:"))
for x in range(1,n+1):
    for y in range(n-x):
        print(end=" ")
    for z in range(1,x+1):
        if z==1:
            print(z,end=" ")
        elif z==x:
           print(z,end=" ")
        elif x==n:
            print(z,end=" ")
        else:
            print(end="  ")
    print()    

        
