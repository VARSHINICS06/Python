# Usinf built in function math.gcd()

# import math
# print(math.gcd(32,80))

# Using loop
# a=4
# b=80
# gvd=-1
# for i in range(1,min(a,b)+1):
#     if(a%i==0 and b%i==0):
#         gcd=i
# print(gcd)

# Euclidean algorithm
# a=52
# b=10
# while(a>0 and b>0):
#     if(a>b):
#         a=a%b
#     else:
#         b=b%a
# if a==0:
#      print(b)
# else:
#      print(a)

def fun_name(i,n):
    if(i>n):
        return
    print("varshini")
    fun_name(i+1,n)
fun_name(1,6)

