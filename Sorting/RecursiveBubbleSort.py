
def rbs(a,n):
    if n==0 or n==1:
        return a
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    return rbs(a,n-1)


a=list(map(int,input("a:").split()))
print(rbs(a,len(a)))