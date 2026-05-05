# 188. Best Time to Buy and Sell Stock IV

# Make atmost K transations
def bs3(a,i,buy,t):
    if i==len(a) or t==0:
        return 0
    ans=float("-inf")
    if buy:
        ans=max(-a[i]+bs3(a,i+1,False,t),bs3(a,i+1,True,t))
    else:
        ans=max(a[i]+bs3(a,i+1,True,t-1),bs3(a,i+1,False,t))
    return ans

# memoization
class Solution:
    def maxProfit(self,t,a) -> int:
        def bs3(i, buy, t):
            if i == len(a) or t == 0:
                return 0
            
            if dp[i][buy][t] != -1:
                return dp[i][buy][t]
            
            if buy:
                ans = max(
                    -a[i] + bs3(i+1, 0, t),   # buy
                    bs3(i+1, 1, t)            # skip
                )
            else:
                ans = max(
                    a[i] + bs3(i+1, 1, t-1),  # sell
                    bs3(i+1, 0, t)            # skip
                )
            
            dp[i][buy][t] = ans
            return ans
        
        n = len(a)
        dp = [[[-1]*(t+1) for _ in range(2)] for _ in range(n)]
        
        return bs3(0, 1, t)
    


# Tabultaion...
class Solution:
    def maxProfit(self,t,a) -> int:
        dp = [[[0]*(t+1) for _ in range(2)] for _ in range(len(a)+1)]
        # base case
        for i in range(len(a)-1,-1,-1):
            for j in range(2):
                for k in range(t):
                    # fill dp
                    if j==1:
                                ans = max(
                                    -a[i] +dp[i+1][0][k],dp[i+1][1][k] 
                                )
                    else:
                                
                                ans = max(
                                    a[i] + dp[i+1][1][k+1],
                                    dp[i+1][0][k]
                                )
                            
                    dp[i][j][k] = ans
        return dp[0][1][0]


#Space optimization....
# memoization
class Solution:
    def maxProfit(self,t,a) -> int:
        dp = [[0]*(t+1) for _ in range(2)] 
        # base case
        for i in range(len(a)-1,-1,-1):
            x = [[0]*(t+1) for _ in range(2)] 
            for j in range(2):
                for k in range(t):
                    # fill dp
                    if j==1:
                                ans = max(
                                    -a[i] +dp[0][k],dp[1][k] 
                                )
                    else:
                                
                                ans = max(
                                    a[i] + dp[1][k+1],
                                    dp[0][k]
                                )
                            
                    x[j][k] = ans
            dp=x
        return x[1][0]
