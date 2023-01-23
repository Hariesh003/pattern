n=int(input("enter n:"))
for x in range(1,n+1):
    for y in range(n-x):
        print(end=" ")
    for z in range(1,x+1):
        print("*",end=" ")
    print()    
