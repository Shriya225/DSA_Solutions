# smallest index of ele where ele>target starts
def upperBound(a,t):
    l,h=0,len(a)-1
    ans=-1
    while l<=h:
        m=(l+h)//2
        if a[m]>t:
            ans=m
            h=m-1
        else:
            l=m+1
    print("ans:",ans)
a=list(map(int,input("a:").split()))
t=int(input("T:"))
upperBound(a,t)  