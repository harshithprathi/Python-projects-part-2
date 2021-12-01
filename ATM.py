a=input().split()
x=int(a[0])
y=a[1].split(".")
z=int(y[0])
if(x%5==0 and x<z):
    print("{:.2f}".format(z-x-0.5))
else:
    print(str(z)+".00")
a=int(input())
b=float(input())
if(a%5==0 and a<b):
    print("{:.2f}".format(b-a-0.5))
else:
    print(b)
