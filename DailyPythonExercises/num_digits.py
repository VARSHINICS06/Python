num=56778686
count=0
while num>0:
    last_dig=num%10
    count+=1
    num=num//10

print(count)