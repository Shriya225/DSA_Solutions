# Longest Common Substring (GFG)


# Brute force
# iterative

# 1.create all substrss of s1,  O(n*2)
#2. check if it exists in s2  ,O(m)
# TC- O(n^2 * m)
def longestCommonSubstring(s1, s2):
    n = len(s1)
    ans = 0

    # generate all substrings of s1
    for i in range(n):
        for j in range(i, n):
            sub = s1[i:j+1]

            # check if substring exists in s2
            if sub in s2:
                ans = max(ans, len(sub))

    return ans


# recursive idea
# Y don't we find longest common suffix 
# for all possible (i,j) pairs
# find max(all lcSuffixes)

# Length of the Longest Common Substring = Max of lengths of all Longest Common Suffixes  

# Length of the Longest Common Suffix Ending at
# (i, j)  = Length of Longest Common Suffix Ending at (i-1, j-1) + 1 if s1[i] == s2[j], else 0  
 
#  Tc-O(n⋅m⋅min(n,m))
def lcs(a,b):
    def lsuffix(a,b,i,j):
        if i<0 or j<0 or a[i]!=b[j]:
            return 0
        return 1+lsuffix(a,b,i-1,j-1)
    ans=0
    for i in range(len(a)):
        for j in range(len(b)):
            ans=max(ans,lsuffix(a,b,i,j))
    return ans

# memoization
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[-1]*m for _ in range(n)]

    def lsuffix(i, j):
        if i < 0 or j < 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        if a[i] == b[j]:
            dp[i][j] = 1 + lsuffix(i-1, j-1)
        else:
            dp[i][j] = 0

        return dp[i][j]

    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, lsuffix(i, j))

    return ans

# tabultaion..

def lcs_tab(a,b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    ans = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1]==b[j-1]:
                dp[i][j]+=1
                if dp[i-1][j-1]!=0:
                    dp[i][j]+=dp[i-1][j-1]
            ans=max(ans,dp[i][j])


# space optimized
def lcs_tab(a,b):
    n, m = len(a), len(b)
    dp = [0]*(m+1)
    ans = 0

    for i in range(1, n+1):
        x=[0]*(m+1)
        for j in range(1, m+1):
            if a[i-1]==b[j-1]:
                x[j] = 1 + dp[j-1]
            ans=max(ans,x[j])
        dp=x
    return ans


# chat gpt one.. (check it out..)
def lcs_substring(s1, s2, i, j, count):
    # base case
    if i == 0 or j == 0:
        return count

    # case 1: characters match → extend substring
    if s1[i-1] == s2[j-1]:
        count = lcs_substring(s1, s2, i-1, j-1, count + 1)

    # case 2: characters don't match → break substring
    # try fresh from other possibilities
    return max(
        count,
        lcs_substring(s1, s2, i-1, j, 0),
        lcs_substring(s1, s2, i, j-1, 0)
    )


def longestCommonSubstring(s1, s2):
    return lcs_substring(s1, s2, len(s1), len(s2), 0)

