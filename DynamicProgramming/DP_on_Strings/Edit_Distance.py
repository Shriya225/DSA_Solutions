# 72. Edit Distance

def ed(a,b,i,j):
   # base cases
    if i < 0:
        return j + 1  # insert all remaining chars of b
    if j < 0:
        return i + 1  # delete all remaining chars of a
    
    if a[i]==b[j]:
        return ed(a,b,i-1,j-1)
    insert=delete=replace=float('inf')
    insert=1+ed(a,b,i,j-1)
    delete=1+ed(a,b,i-1,j)
    replace=1+ed(a,b,i-1,j-1)
    return min(insert,replace,delete)


# memoization
class Solution:
    def minDistance(self, a,b) -> int:
        def ed(a,b,i,j,dp):
        # base cases
            if i < 0:
                return j + 1  # insert all remaining chars of b
            if j < 0:
                return i + 1  # delete all remaining chars of a
            
            if dp[i][j]!=-1:return dp[i][j]

            if a[i]==b[j]:
                return ed(a,b,i-1,j-1,dp)
            insert=delete=replace=float('inf')
            insert=1+ed(a,b,i,j-1,dp)
            delete=1+ed(a,b,i-1,j,dp)
            replace=1+ed(a,b,i-1,j-1,dp)
            dp[i][j]=min(insert,replace,delete)
            return dp[i][j]
        dp=[[-1]*len(b) for i in range(len(a))]
        return ed(a,b,len(a)-1,len(b)-1,dp)



# Tabulation
class Solution:
    def minDistance(self, a,b) -> int:
        dp=[[0]*(len(b)+1) for i in range(len(a)+1)]
        # base case
        for i in range(1,len(a)+1):
            dp[i][0]=i
        for j in range(1,len(b)+1):
            dp[0][j]=j
        # fill dp
        for i in range(1,len(a)+1):
            for j in range(1,len(b)+1):
                if a[i-1]==b[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    insert=delete=replace=float('inf')
                    insert=1+dp[i][j-1]
                    delete=1+dp[i-1][j]
                    replace=1+dp[i-1][j-1]
                    dp[i][j]=min(insert,replace,delete)
        return dp[-1][-1]
    
# space optimization
class Solution:
    def minDistance(self, a,b) -> int:
        dp=[0]*(len(b)+1)
        # base case
        for j in range(1,len(b)+1):
            dp[j]=j
        # fill dp
        for i in range(1,len(a)+1):
            x=[0]*(len(b)+1)
            x[0]=i
            for j in range(1,len(b)+1):
                if a[i-1]==b[j-1]:
                    x[j]= dp[j-1]
                else:
                    insert=delete=replace=float('inf')
                    insert=1+x[j-1]
                    delete=1+dp[j]
                    replace=1+dp[j-1]
                    x[j]=min(insert,replace,delete)
            dp=x
        return dp[-1]
    


        
    



