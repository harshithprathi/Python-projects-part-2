a=int(input())
if((str(a)[0]!=str(a)[1]) or (str(a)[2]!=str(a)[3]) or (str(a)[0]!=str(a)[2]) or (str(a)[1]!=str(a)[3]) or (str(a)[0]!=str(a)[3]) or (str(a)[1]!=str(a)[2])):
    a+=1
    while((str(a)[0]==str(a)[1]) or (str(a)[2]==str(a)[3]) or (str(a)[0]==str(a)[2]) or (str(a)[1]==str(a)[3]) or (str(a)[0]==str(a)[3]) or (str(a)[1]==str(a)[2])):
        a+=1
else:
    while((str(a)[0]==str(a)[1]) or (str(a)[2]==str(a)[3]) or (str(a)[0]==str(a)[2]) or (str(a)[1]==str(a)[3]) or (str(a)[0]==str(a)[3]) or (str(a)[1]==str(a)[2])):
        a+=1    
print(a)
