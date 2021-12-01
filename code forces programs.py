
#next round
'''n=input().split()
m=input().split()
x=int(n[0])
y=int(n[1])
p=0
for i in range(0,x):
     if(int(m[i])>=int(m[y-1]) and int(m[i])>0):
         p+=1
print(p)'''
#team
'''
n=int(input())
x=0
for i in range(n):
    a=input().split()
    c=0
    for i in a:
        if(i=='1'):
            c+=1
    if(c==2 or c==3):
        x+=1
print(x)'''
#from math import ceil
#print(ceil(1.5))
#Way too long words
'''n=int(input())
for i in range(n):
    s=input()
    if(len(s)<=10):
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[-1])'''
#square area
'''a=input().split()
x=int(a[0])
y=int(a[1])
area=x*y
if(area%2==0):
    print(int(area/2))
else:
    print(int((area-1)/2))'''
#bit++
'''n=int(input())
p=0
for i in range(n):
    s=input()
    if(s=="--X" or s=="X--"):
        p-=1
    if(s=="++X" or s=="X++"):
        p+=1
print(p)'''
#petya and strings
'''a=input()
b=input()
if(a.upper()==b.upper()):
    print("0")
elif(a.upper()>b.upper()):
    print("1")
else:
    print("-1")
    '''
# string task
'''n=input().lower()
l=[]
for i in range(len(n)):
    if(n[i]!="a" and n[i]!="e" and n[i]!="i" and n[i]!="o" and n[i]!="u" and n[i]!="y"):
        l.append(n[i])
print(".",end="")
for i in range(len(l)-1):
    print(l[i],end=".")
print(l[-1],end="")'''
#helpful maths
'''a=input()
i=0
s=""
r=""
while(i<len(a)):
    if(i==0 or i%2==0):
        s=s+a[i]
    else:
        r=r+a[i]
    i+=1
x=sorted(list(s))
y=list(r)
for i in range(len(x)):
    print(x[i],end="")
    if(i<len(y)):
        print(y[i],end="")'''
#capitalize
'''a=input()
print(a[0].upper()+a[1:])
'''
#stones on the table
'''n=int(input())
a=input()
c=0
for i in range(n-1):
    if(a[i]==a[i+1]):
        c+=1
print(c)
        '''
#boy or girl
'''a=input()
b=''.join(set(a))
if(len(b)%2==0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")'''
#foot ball
'''a=input()
if(("0000000" in a) or ("1111111" in a)):
    print("YES")
else:
    print("NO")
'''
#soldier and bananas
'''a=input().split()
x=int(a[0])
y=int(a[1])
z=int(a[2])
b=0
for i in range(1,z+1):
    b=x*i+b
if(b-y>0):
    print(b-y)
else:
    print("0")
'''
#bear and big brother
'''a=input().split()
x=int(a[0])
y=int(a[1])
c=0
while(y>=x):
    x=x*3
    y=y*2
    c+=1
print(c)'''
#elephant
'''a=int(input())
p=a//5
if(a%5>0):
    p+=1
print(p)'''
#wrong subtraction
'''a=input().split()
x=int(a[0])
y=int(a[1])
for i in range(y):
    if(x%10==0):
        x=x//10
    else:
        x=x-1'''
#word
'''a=input()
b=0
c=0
for i in a:
    if(i.islower()):
        b+=1
    else:
        c+=1
if(b>=c):
    print(a.lower())
else:
    print(a.upper())'''
#tram
'''n=int(input())
c=0
l=[]
for i in range(n):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    c=c+(x-y)
    l.append(abs(c))
print(max(l))'''
#Chat room
'''import re
a=input()
if re.match('.*h.*e.*l.*l.*o.*', a):
    print("YES")
else:
    print("NO")'''
#nearly lucky number
'''a=input()
c=0
for i in a:
    if(i=="4" or i=="7"):
        c+=1
if(c==4 or c==7):
    print("YES")
else:
    print("NO")'''
#Lucky division
'''a=int(input())
if(a%4==0 or a%7==0 or a%47==0 or a%74==0 or a%774==0 or a%747==0 or a%477==0 or a%44==0 or a%77==0 or a%444==0 or a%777==0 or a%474==0):
    print("YES")
else:
    print("NO")'''
n=int(input())
c=0
for i in range(n):
    s=input().split()
    a=int(s[0])
    b=int(s[1])
    if(a!=b):
        c+=1
print(c)





























        
    
