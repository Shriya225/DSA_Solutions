# right ot left.
def SellStock(a):
    maxele=0
    ans=0
    for i in range(len(a)-1,-1,-1):
        maxele=max(maxele,a[i])
        ans=max(maxele-a[i],ans)
    return ans
        
a=list(map(int,input("a:").split()))
print(SellStock(a))


# left to right
def SellStock(a):
    minele=a[0]
    ans=0
    for i in range(len(a)):
        ans=max(ans,a[i]-minele)
        minele=min(minele,a[i])
    return ans
        
a=list(map(int,input("a:").split()))
print(SellStock(a))