# bactarck on tabualted code..
def lcs_tab(a,b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    ans = 0
    p=q=0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1]==b[j-1]:
                dp[i][j]+=1
                if dp[i-1][j-1]!=0:
                    dp[i][j]+=dp[i-1][j-1]
            # track amx..
            if dp[i][j]>ans:
                ans=dp[i][j]
                p=i-1
                q=j-1
    
    # backtrack to find answer...
    ans=""
    while p>0 and q>0:
        ans=a[p]+ans
        p-=1
        q-=1
    return ans

a=input("a:")
b=input("b:")
print(lcs_tab(a,b))
