
def ReverseArr(s,l,r):
    if l>=r:
        return s
    s[l],s[r]=s[r],s[l]
    return ReverseArr(s,l+1,r-1)
s=list(map(int,input("a:").split()))
print(ReverseArr(s,0,len(s)-1))