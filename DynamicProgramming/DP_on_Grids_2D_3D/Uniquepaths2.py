# 63. Unique Paths II


# reccurence reln
def uq2(a,m,n,i,j):
    if i==0 and j==0:
        return 1
    if i<0 or j<0:return 0
    w=0
    if a[i][j]==1:return 0
    w+=uq2(a,m,n,i-1,j)
    w+=uq2(a,m,n,i,j-1)
    return w


# memoization
# reccurence reln
def uq2(a,m,n,i,j,dp):
    if i<0 or j<0:return 0
    if a[i][j]==1:return 0
    if i==0 and j==0:
        return 1
    w=0
    if dp[i][j]!=-1:return dp[i][j]
    w+=uq2(a,m,n,i-1,j,dp)
    w+=uq2(a,m,n,i,j-1,dp)
    dp[i][j]=w
    return w


# tabulation..

def uq2_tab(a,m,n,i,j):
    dp = [[0]*n for _ in range(m)]
    dp[0][0]=1
    if a[0][0]==1:return 0
    for i in range(m):
        for j in range(n):
           if i==0 and j==0:
               continue
           w=0
           if a[i][j]==0:
                if i-1>=0:
                    w+=dp[i-1][j]
                if j-1>=0: 
                    w+=dp[i][j-1]
           dp[i][j]=w
    return dp[m-1][n-1]


# sapce optimization...
           
def uq2_tab2(a,m,n,i,j):
    dp = [0]*n
    dp[0]=1
    if a[0][0]==1:return 0
    for i in range(m):
        x=[0]*n
        for j in range(n):
           if i==0 and j==0:
               x[0]=1
               continue
           w=0
           if a[i][j]==0:
                if i-1>=0:
                    w+=dp[j]
                if j-1>=0: 
                    w+=x[j-1]
           x[j]=w
        dp=x
    return dp[n-1]
            
