def compress(s):
    l=len(s)
    i=0
    while i<l:
        c=1
        while (i<l-1 and s[i]==s[i + 1]):
            c+=1
            i+=1
        i+=1
        print(s[i - 1]+str(c),end = "")
if __name__ == "__main__":
    s=input()
    compress(s)
