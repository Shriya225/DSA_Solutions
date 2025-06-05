# 540. Single Element in a Sorted Array
def singleEle(a):
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]!=a[m-1] and a[m]!=a[m+1]:
            return a[m]
        if a[0]!=a[1]:
            return a[0]
        if a[-1]!=a[-2]:
            return a[-1]
        elif a[m]==a[m+1]:
            if (len(a)-m)%2==0:
                h=m-1
            else:
                l=m+1
        elif a[m]==a[m-1]:
            if (m+1)%2==0:
                l=m+1
            else:
                h=m-1
    return -1
a=list(map(int,input("A:").split()))
print(singleEle(a))