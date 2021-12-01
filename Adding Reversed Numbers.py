n=int(input())
for i in range(n):
    st=input().split()
    x=int(st[0])
    y=int(st[1])
    s=0
    r=0
    ab=0
    while(x!=0):
        n=x%10
        s=s*10+n
        x=x//10
    m=s
    while(y!=0):
        p=y%10
        r=r*10+p
        y=y//10
    k=r
    summ=m+k
    while(summ!=0):
        mn=summ%10
        ab=ab*10+mn
        summ=summ//10
    print(ab)
    


