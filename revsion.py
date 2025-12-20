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

a=list(map(int,input("a:").split()))
t=int(input("t:"))
print(bs(a,t))