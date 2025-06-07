# Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X 
# such that when X is raised to the power of N, 
# it equals M. If the Nth root is not an integer, return -1.
def nthRoot(n,p):
    l,h=0,n//2
    while l<=h:
        m=(l+h)//2
        if m**p==n:
            return m
        elif (m**p)>n:
            h=m-1
        else:
            l=m+1
    return -1

n=int(input("n:"))
p=int(input("p:"))
print(nthRoot(n,p))