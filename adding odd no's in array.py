a=int(input())
b=input().split()
d=0
i=0
for i in b:
    if(int(i)%2!=0):
        d=d+int(i)
print(d)
