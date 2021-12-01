n=int(input())
for i in range(n):
    st=int(input())
    j=1
    s=st
    while(j<st):
        s=s*j
        j+=1
    a=s
    c=0
    while(a%10==0):
        c+=1
        a=a//10
    print(c)
        
        
    

