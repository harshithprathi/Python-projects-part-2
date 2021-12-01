'''a=0
b=1
n=int(input())
if n==1:
    print(a)
if n==2:
    print(b)
if n>2:
    print(a)
    print(b)
    for i in range(0,n-1):
        c=a+b
        a=b
        b=c
        print(c)#print n terms
print(c)#print's nth term'''
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i)) #prints n terms 
print(recur_fibo(nterms-1))#prints nth term
