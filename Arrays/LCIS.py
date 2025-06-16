# 674. Longest Continuous Increasing Subsequence length
def LCIS(a):
    c=maxc=0
    for i in range(len(a)):
        if i<len(a)-1:
            if a[i]<a[i+1]:
                c+=1
            else:
                maxc=max(c+1,maxc)
                c=0
        maxc=max(c,maxc)
        if i==len(a)-1:
            maxc=max(c+1,maxc)
    print(maxc)

def LCIS2(a):
    c=maxc=1
    if not a:
        return 0
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            c+=1
        else:
            c=1
        maxc=max(c,maxc)
    print("maxc")
l=list(map(int,input("a:").split()))
LCIS(l)
