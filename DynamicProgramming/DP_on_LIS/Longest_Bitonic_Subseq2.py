# Optimal approach using LIS and LDS

class Solution:
    def longestBitonicSequence(self, n, a):
            n = len(a)
        
            # LDS from right
            dp = [1] * n
        
            for i in range(n - 1, -1, -1):
        
                for j in range(n - 1, i, -1):
        
                    if a[i] > a[j]:
                        dp[i] = max(dp[i], 1 + dp[j])
        
            # LIS from left
            dp2 = [1] * n
        
            for i in range(n):
        
                for j in range(i):
        
                    if a[i] > a[j]:
                        dp2[i] = max(dp2[i], 1 + dp2[j])
        
            ans = 0
        
            for i in range(n):
                if dp[i]>1 and dp2[i]>1:
                    ans = max(ans, dp[i] + dp2[i] - 1)
        
            return ans
        
    