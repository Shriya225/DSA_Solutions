# 518. Coin Change II

# reccurence rel'n
class Solution:
    def change(self, t: int, a) -> int:
        def cc2(a,t,i):
            if t==0:
                return 1
            if i<0: 
                    return 0 
            l=cc2(a,t,i-1)
            r=0
            if a[i]<=t: 
                r=cc2(a,t-a[i],i)
            return l+r
        return cc2(a,t,len(a)-1)
    
# memoization...

class Solution:
    def change(self, t: int, a) -> int:
        def cc2(a,t,i,dp):
            if t==0:
                return 1
            if i<0: 
                    return 0 
            if dp[i][t]!=-1:return dp[i][t]
            l=cc2(a,t,i-1,dp)
            r=0
            if a[i]<=t: 
                r=cc2(a,t-a[i],i,dp)
            dp[i][t]=l+r
            return l+r
        dp=[[-1]*(t+1) for i in range(len(a))]
        return cc2(a,t,len(a)-1,dp)
    
# tabulate...

class Solution:
    def change(self, t: int, a) -> int:
        dp=[[0]*(t+1) for i in range(len(a))]
        # base case
        # base case: sum = 0
        for i in range(len(a)):
            dp[i][0] = 1
        for i in range(a[0],t+1):
            if i%a[0]==0:
                 dp[0][i]=1
        # fill dp
        for i in range(1,len(a)):
            for j in range(t+1):
                l=dp[i-1][j]
                r=0
                if a[i]<=j: 
                    r=dp[i][j-a[i]]
                dp[i][j]=l+r
        return dp[-1][-1]
         
        
# space optimize..
class Solution:
    def change(self, t: int, a) -> int:
        dp=[0]*(t+1) 
        # base case
        # base case: sum = 0
        dp[0] = 1
        for i in range(a[0],t+1):
            if i%a[0]==0:
                 dp[i]=1
        # fill dp
        for i in range(1,len(a)):
            for j in range(a[i],t+1):
                l=dp[j]
                r=0
                if a[i]<=j: 
                    r=dp[j-a[i]]
                dp[j]=l+r
        return dp[-1]
         
 