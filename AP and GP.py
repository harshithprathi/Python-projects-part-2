while(1):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    z=int(a[2])
    while(x or y or z):
        if(y-x==z-y):
            print("AP",z+(z-y))
            break
        else:
            print("GP",int(z*(z/y)))
            break
    if(x==0 and y==0 and z==0):
                break
