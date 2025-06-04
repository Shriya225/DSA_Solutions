# least index  where ele>=target
# from lowerbound all eles are greater than or = to target
def lowerBound(a,t):
    l=0
    ans=-1
    h=len(a)-1
    # if all ele are less than t,then no ans 
    if a[-1]<t:
        return -1
    # if all ele are > t,ele 0 is ans
    if a[0]>=t:
        return 0
    while l<=h:
        m=(l+h)//2
        if a[m]>=t:
            ans=m
            h=m-1
        else:
            l=m+1
    print("ans: ",ans)
a=list(map(int,input("a:").split()))
t=int(input("T:"))
lowerBound(a,t)  