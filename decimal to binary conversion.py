n=int(input())
for i in range(n):
    a=int(input())
    c=bin(a)
    print(c[2:])




     #or
'''
n=int(input())
for i in range(n):
    a=int(input())
    s=a
    c=""
    while(s>=1):
        c=c+str(s%2)
        s=s//2
    print(c[::-1])
        '''
