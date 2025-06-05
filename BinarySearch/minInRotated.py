# 153. Find Minimum in Rotated Sorted Array
def minEle(a):
    if a[0]<=a[-1]:
        return a[0]
    l,h=0,len(a)-1
    ans=-1
    while l<=h:
        m=(l+h)//2
        print(m,a[m])
        if a[m]<a[0]:
            ans=m
            h=m-1
        else:
            l=m+1
    return a[ans]

a=list(map(int,input("a:").split()))
print(minEle(a))