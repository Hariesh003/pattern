n=int(input("enter n:"))
for x in range(1,n+1):
    for y in range(1,x+1):
         if x==y:
             print("*",end=" ")
         else:
             print(end="   ")
    print() 
