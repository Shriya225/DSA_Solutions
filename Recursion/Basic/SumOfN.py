# Sum of first N natural numbers
def sumOfN(n,s=0):
    if n==0:
        return s
    return sumOfN(n-1,s+n)
k=int(input("k:"))
print(sumOfN(k))