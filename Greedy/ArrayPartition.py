# 561. Array Partition
class Solution:
    def arrayPairSum(self, a):
        a.sort()
        ans=0
        i=0
        while i<len(a):
            ans+=min(a[i],a[i+1])
            i+=2
        return ans
        