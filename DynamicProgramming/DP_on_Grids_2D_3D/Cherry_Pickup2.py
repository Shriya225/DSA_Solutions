# 1463. Cherry Pickup II

# reccurence rel'n
def nfriends(a,i,j1,j2):
    if j1<0 or j1>=len(a[0]) or j2<0 or j2>=len(a[0]):
        return float("-inf")
    if i==len(a)-1:
        if j1!=j2:
            return a[i][j1]+a[i][j2]
        else:
            return a[i][j1]
    val= a[i][j1]+a[i][j2] if j1!=j2 else a[i][j1]
    z=[[0,0],[0,-1],[0,1],[1,1],[-1,-1],[1,-1],[1,0],[-1,0],[-1,1]]
    ans=float("-inf")
    for x,y in z:
        ans=max(ans,nfriends(a,i+1,j1+x,j2+y))
    return val+ans

# memoization
def nfriends_memo(a,i,j1,j2,dp):
        if j1<0 or j1>=len(a[0]) or j2<0 or j2>=len(a[0]):
            return float("-inf")
        if i==len(a)-1:
            if j1!=j2:
                return a[i][j1]+a[i][j2]
            else:
                return a[i][j1]
        if dp[i][j1][j2]!=-1:return dp[i][j1][j2]
        val= a[i][j1]+a[i][j2] if j1!=j2 else a[i][j1]
        z=[[0,0],[0,-1],[0,1],[1,1],[-1,-1],[1,-1],[1,0],[-1,0],[-1,1]]
        ans=float("-inf")
        for x,y in z:
            ans=max(ans,nfriends_memo(a,i+1,j1+x,j2+y,dp))
        dp[i][j1][j2]=val+ans
        return dp[i][j1][j2]

# tabualtion
def nfrie_tab(a):
        m,n=len(a),len(a[0])
        dp=[[[-1]*n for _ in range(n)]for _ in range(m)]
        # base case..
        for i in range(n):
            for j in range(n):
                if i!=j:
                    dp[m-1][i][j]=a[m-1][i]+a[m-1][j]
                else:
                    dp[m-1][i][j]=a[m-1][i]
        # tabualtion code..
        for r in range(m-2,-1,-1):
            for i in range(n):
                for j in range(n):
                    val= a[r][j]+a[r][i] if i!=j else a[r][j]
                    z=[[0,0],[0,-1],[0,1],[1,1],[-1,-1],[1,-1],[1,0],[-1,0],[-1,1]]
                    ans=float("-inf")
                    for x,y in z:
                        if 0<=i+x<n and 0<=j+y<n:
                            ans=max(ans,dp[r+1][i+x][j+y])
                    dp[r][i][j]=val+ans
        return dp[0][0][n-1]


# space optimized...
# 3d Dp to 2D Dp
def nfrie_tab2(a):
        m,n=len(a),len(a[0])
        dp=[[-1]*n for _ in range(n)]
        # base case..
        for i in range(n):
            for j in range(n):
                if i!=j:
                    dp[i][j]=a[m-1][i]+a[m-1][j]
                else:
                    dp[i][j]=a[m-1][i]
        # tabualtion code..
        for r in range(m-2,-1,-1):
            temp=[[-1]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    val= a[r][j]+a[r][i] if i!=j else a[r][j]
                    z=[[0,0],[0,-1],[0,1],[1,1],[-1,-1],[1,-1],[1,0],[-1,0],[-1,1]]
                    ans=float("-inf")
                    for x,y in z:
                        if 0<=i+x<n and 0<=j+y<n:
                            ans=max(ans,dp[i+x][j+y])
                    temp[i][j]=val+ans
            dp=temp
        return dp[0][n-1]

        
                     
    

    