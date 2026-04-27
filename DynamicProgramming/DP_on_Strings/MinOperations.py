# 583. Delete Operation for Two Strings

# space otpimized lcsubseq
class Solution:
    def minDistance(self, a: str,b: str) -> int:
        def longestCommonSubsequence( a, b) -> int:
            n, m = len(a), len(b)
            
            dp = [0]*m   # previous row

            # base case (row 0)
            for j in range(m):
                if a[0] == b[j]:
                    dp[j] = 1
                elif j > 0:
                    dp[j] = dp[j-1]
            # fill
            for i in range(1, n):
                x = [0]*m   # current row
                
                for j in range(m):
                    if a[i] == b[j]:
                        if j > 0:
                            x[j] = 1 + dp[j-1]
                        else:
                            x[j] = 1
                    else:
                        up = dp[j]
                        left = x[j-1] if j > 0 else 0
                        x[j] = max(up, left)
                
                dp = x   # move current → previous
            return dp[-1]
        return (len(a)+len(b))-2*(longestCommonSubsequence(a,b))