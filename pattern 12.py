n=int(input("enter n:"))
for x in range(1,n+1):
    val=x
    dec=n-1
    for y in range(1,x+1):
        print(val,end=" ")
        val=val+dec
        dec=dec-1
    print()
