# prefix & suffix sum logic
# o(n)
def PivotIndex(a):
    n=len(a)
    prefix=[-1]*(n)
    suffix=[-1]*(n)
    for i in range(n):
        if i==0:
            prefix[0]=a[i]
            suffix[n-i-1]=a[n-i-1]
        else:
            prefix[i]=prefix[i-1]+a[i]
            suffix[n-i-1]=suffix[n-i]+a[n-i-1]
    print("prefix",prefix,"suffix",suffix)
    for i in range(n):
        if prefix[i]-a[i]==suffix[i]-a[i]:
            print("pivot index is :",i,a[i])
a=list(map(int,input("a:").split()))
PivotIndex(a)