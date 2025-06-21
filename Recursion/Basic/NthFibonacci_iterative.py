# iterative approach
def nthFib(n):
    if n==1 or n==2:
        return n-1
    n1,n2=0,1
    ans=0
    for i in range(n-2):
        ans=n1+n2
        n1=n2
        n2=ans
    return ans

n=int(input("n:"))
print(nthFib(n))