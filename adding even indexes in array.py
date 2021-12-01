a=int(input())
b=input().split()
d=0
i=0
while(i<a):
    if(i==0 or i%2==0):
        d=d+int(b[i])
    i=i+1
print(d)
