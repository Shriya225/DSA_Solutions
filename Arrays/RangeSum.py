# 303. Range Sum Query - Immutable
# Prefix sum example
# o(n)
class NumArray:

    def __init__(self, nums):
        self.nums=nums
        self.prefix={}
        s=0
        for i in range(len(self.nums)):
            s+=self.nums[i]
            self.prefix[i]=s

    def sumRange(self, l: int, r: int) -> int:
        if l==0:
            return self.prefix[r]
        return self.prefix[r]-self.prefix[l-1]