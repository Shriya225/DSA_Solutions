# 121. Best Time to Buy and Sell Stock

# Make  1 transations
class Solution:
    def maxProfit(self,a) -> int:
        m=a[-1]
        ans=0
        for i in range(len(a)-1,-1,-1):
            if a[i]>m:
                m=a[i]
            else:
                ans=max(ans,m-a[i])
        return ans