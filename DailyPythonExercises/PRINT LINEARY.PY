def LINEAR(i,N):
    if(i>N):
        return
    print(i)
    LINEAR(i+1,N)

i=int(input("Enter starting digite:"))
n=int(input("Enter ending digite:"))
LINEAR(i,n)

