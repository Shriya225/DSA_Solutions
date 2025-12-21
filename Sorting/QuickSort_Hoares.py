# 1st ele as pivot.
def partition(a,l,h):
    if l>=h:
        return 
    pivot=a[l]
    i,j=l,h
    while i<j:
        while i<h and a[i]<=pivot:
            i+=1
        while a[j]>pivot:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[j],a[l]=a[l],a[j]
    return j
def qs(a,l,h):
    if l<h:
        pi=partition(a,l,h)
        qs(a,l,pi-1)
        qs(a,pi+1,h)


a=list(map(int,input("a:").split()))
print(qs(a,0,len(a)-1))
print(a)
