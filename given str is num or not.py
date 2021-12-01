a=input()
count=0
for i in a:
    if(i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9" or i=="0"):
        count+=1
if(count==len(a)):
    print("Yes")
else:
    print("No")
