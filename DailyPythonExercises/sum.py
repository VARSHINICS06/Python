# def summ(i,n):
#     if(i<1):
#         print(n)
#         return
#     summ(i-1,n+i)
# summ(2,0)

def sumn(n):
    if n==0:
        return 0
    return n+sumn(n-1)
print(sumn(5))