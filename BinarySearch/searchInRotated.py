# 33. Search in Rotated Sorted Array
def bs(a,t):
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            return m
        elif a[m]>t:
            h=m-1
        else:
            l=m+1
    return -1

def searchInRotated(a,t):
    if a[0]<a[-1]:
        return bs(a,t)
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        print(m,a[m])
        if a[m]==t:
            return m
        if a[-1]<t<a[0]:
            return -1
        if a[m]>=a[0] and a[0]<=t<a[m]:
            h=m-1
        elif a[m]>=a[0] and (t>a[m] or t<a[0]):
            l=m+1
        elif a[m]<a[0] and a[m]<t<=a[-1]:
            l=m+1
        
        elif a[m]<a[0] and (t<a[m] or t>=a[0]):
            h=m-1
    return -1

a=list(map(int,input("a:").split()))
t=int(input("T:"))
print(searchInRotated(a,t))  