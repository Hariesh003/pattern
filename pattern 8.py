n=int(input("enter n:"))
number=1
for x in range(1,n+1):
   for y in range(1,x+1):
    print(number,end=" ")
    number+=1
   print() 
