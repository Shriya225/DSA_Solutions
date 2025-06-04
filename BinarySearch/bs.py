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