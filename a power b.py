n=int(input())
for i in range(n):
    m=list(map(int, input().split()))
    x,ans=m[0],1
    b=m[1]
    while(b!=0):
        if(b&1==1):
            ans=(ans*x)%1000000007
        x=(x*x)%1000000007
        b=b>>1        
    print(int(ans%1000000007))
