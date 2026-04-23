# using perfect sum problem here....

class Solution:
    def findTargetSumWays(self, a, t):
        def perfectSum( a,k):
            n = len(a)
            dp = [0]*(k+1)
        
            # base case
            dp[0] = 1
            # at index 0 ele place 1
            if a[0] <= k:
                dp[a[0]] += 1
        
            if a[0] == 0:
                dp[0] = 2
        
            # tabulation
            for i in range(1, n):
                x = [0]*(k+1)
                for j in range(k+1):
                    not_take = dp[j]
                    take = 0
                    if j >= a[i]:
                        take = dp[j - a[i]]
        
                    x[j] = not_take + take
        
                dp = x
        
            return dp[k]
        k=(t+sum(a))//2
        s=sum(a)
        # edge cases
        if (t + s) % 2 != 0:
            return 0
        if abs(t) > s:
            return 0
        return perfectSum(a,k)