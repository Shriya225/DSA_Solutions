# iterative
def bs(a,n,t):
    l=0
    h=n-1
    while l<=h:
        m=(l+h)//2
        if a[m]==t:
            print(f"{t} found at {m} index")
            break
        elif t>a[m]:
            l=m+1
        else:
            h=m-1
    return None

a=list(map(int,input("a:").split()))
t=int(input("T:"))
bs(a,len(a),t)

# recursive func
def bs(a,t,l,h):
    if l>h:
        return -1
    m=(l+h)//2
    if a[m]==t:
        return m
    elif a[m]>t:
        return bs(a,t,l,m-1)
    else:
        return bs(a,t,m+1,h)
