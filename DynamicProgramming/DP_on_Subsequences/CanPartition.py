# 416. Partition Equal Subset Sum

# space optimized code..
class Solution:
    def canPartition(self, a) -> bool:
            # the only change from (subset sum == k) ques
            k=sum(a)//2
            if sum(a)%2!=0:return False


            dp=[-1]*(k+1)
            # base case
            for i in range(k+1):
                if i==0:
                    dp[0]=True
                else:
                    dp[i]=True if a[0]==i else False
            # tabulate..
            for i in range(1,len(a)):
                x=[-1]*(k+1)
                for j in range(k+1):
                    if j==0:
                        x[0]=True
                    else:
                        l=r=False
                        l=dp[j]
                        if j-a[i]>=0:
                            r=dp[j-a[i]]
                        x[j]=l or r
                dp=x
            return dp[k]