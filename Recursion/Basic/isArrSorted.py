
def isArrSorted(a,i=0):
    if i+1==len(a):
        return True
    if a[i]>a[i+1]:
        return False
    return isArrSorted(a,i+1)
a=list(map(int,input("a:").split()))
print(isArrSorted(a))