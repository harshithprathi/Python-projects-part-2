a=int(input("Enter the size of array: "))
b=input().split()
for i in range(0,a):
    for j in range(i+1,a):
        if(b[i]==b[j]):
            print(b[i])
