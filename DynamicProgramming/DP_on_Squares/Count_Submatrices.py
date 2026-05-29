# 1277. Count Square Submatrices with All Ones

# Tabualtion...
class Solution:
    def countSquares(self, a):

        rows = len(a)
        cols = len(a[0])

        dp = [[0]*cols for _ in range(rows)]

        ans = 0

        for i in range(rows):
            for j in range(cols):

                if a[i][j] == 1:

                    if i == 0 or j == 0:
                        dp[i][j] = 1

                    else:
                        dp[i][j] = 1 + min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        )

                    ans += dp[i][j]

        return ans