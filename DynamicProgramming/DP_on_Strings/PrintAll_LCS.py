class Solution:
    def longestCommonSubsequence(self, a, b):
        n, m = len(a), len(b)
        
        # build dp
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        memo = {}
        return self.all_lcs(a, b, dp, n, m, memo)

    def all_lcs(self, a, b, dp, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            return {""}

        if a[i-1] == b[j-1]:
            res = {s + a[i-1] for s in self.all_lcs(a, b, dp, i-1, j-1, memo)}
        else:
            res = set()

            if dp[i-1][j] == dp[i][j]:
                res |= self.all_lcs(a, b, dp, i-1, j, memo)

            if dp[i][j-1] == dp[i][j]:
                res |= self.all_lcs(a, b, dp, i, j-1, memo)

        memo[(i, j)] = res
        return res