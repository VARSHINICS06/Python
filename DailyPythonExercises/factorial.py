def multi(i,n):
    if(i<1):
        print(n)
        return
    multi(i-1,n*i)
multi(2,0)

# def multi(n):
#     if n==1:
#         return 1
#     return n*multi(n-1)
# print(multi(5))