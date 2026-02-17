# gfg
class Solution:
    def isMaxHeap(self,a,n):
        # Your code goes here
        for i in range(n):
            l=2*i+1
            r=2*i+2
            if l<n and a[i]<a[l] or (r<n and a[i]<a[r]):
                return False
        return True