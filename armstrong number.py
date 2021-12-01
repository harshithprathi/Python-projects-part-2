a=int(input())
s=a
c=0
while(s>0):
    n=s%10
    c=c+n**3
    s=s//10
if(a==c):
    print("Yes")
else:
    print("No")
    
    
