# Perfect Sum Problem (GFG)

# Given an array arr of non-negative integers and an integer target, 
# the task is to count all subsets of the array whose sum is equal to the given target.

# reccurenec rel'n
def psum(a,i,t):
    if t==0:
        return 1
    if i==0:
        return 1 if a[i]==t else 0
    l=psum(a,i-1,t-a[i])
    r=psum(a,i-1,t)
    return l+r



# memoization...
class Solution:
    def perfectSum(self, a, t):
        def psum(a,i,t,dp):
            if i==0:
                if t==0:
                    if a[0]==0:
                        return 2
                    return 1
                return 1 if a[i]==t else 0
            if dp[i][t]!=-1:return dp[i][t]
            l=0
            if t-a[i]>=0:
                l=psum(a,i-1,t-a[i],dp)
            r=psum(a,i-1,t,dp)
            dp[i][t]=l+r
            return dp[i][t]
        dp=[[-1]*(t+1) for i in range(len(a))]
        return psum(a,len(a)-1,t,dp)


# tabualtion..
# space optimized...
class Solution:
	def perfectSum(self, a,k):
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


