num=121
rev=0
while num>0:
    last=num%10
    rev=rev*10+last
    num=num//10
if rev==num:
    print("It is a Palindrome number")
print("not a palindrome number")