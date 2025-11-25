num=987
rev_num=0
while num>0:
    last_dig=num%10
    rev_num=rev_num*10+last_dig
    num=num//10
print(rev_num)