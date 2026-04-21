
class Solution:
    def countPartitions(self,a,d):
            # code here
            k=sum(a)
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
            for s1 in range((k//2)+1):
                if abs(s1-(k-s1))==d:
                    return dp[s1]
            
        
        