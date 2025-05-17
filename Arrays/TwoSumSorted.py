# as arr is sorted for each ele k-a[i] can be done using binarySearch.O(nlogn)
# 2-pointer  o(n)
def twoSumSorted(a,k):
    l=0
    r=len(a)-1
    while l<r:
        if a[l]+a[r]==k:
            return [l+1,r+1]
        elif a[l]+a[r]>k:
            r-=1
        else:
            l+=1

l=list(map(int,input("A:").split()))
k=int(input("K:"))
print(twoSumSorted(l,k))
