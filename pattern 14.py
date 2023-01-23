n=int(input("enter n:"))
for x in range(1,n+1):
    for y in range(1,x+1):
        if y%2!=0: 
            print("1",end=" ")
        elif y%2==0:
            print("0",end=" ")
        else:
            print("0",end=" ")
    print()    
