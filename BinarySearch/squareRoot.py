def squareRoot(n):
    l=0
    h=n//2
    ans=-1
    while l<=h:
        m=(l+h)//2
        if m*m==n:
            return m
        elif m*m >n:
            h=m-1
        else:
            ans=m
            l=m+1
    return ans
n=int(input("n:"))
print(squareRoot(n))