# Boolean Parenthesization(GFG)
class Solution:
    def countWays(self, n, s):
        
        dp = {}
        
        def f(i, j, isTrue):
            
            # invalid
            if i > j:
                return 0
            
            # single character
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0
            
            if (i, j, isTrue) in dp:
                return dp[(i, j, isTrue)]
            
            ways = 0
            
            # operators exist at odd indices
            for k in range(i + 1, j, 2):
                
                op = s[k]
                
                lt = f(i, k - 1, True)
                lf = f(i, k - 1, False)
                
                rt = f(k + 1, j, True)
                rf = f(k + 1, j, False)
                
                # AND
                if op == '&':
                    
                    if isTrue:
                        ways += lt * rt
                    else:
                        ways += (lt * rf) + (lf * rt) + (lf * rf)
                
                # OR
                elif op == '|':
                    
                    if isTrue:
                        ways += (lt * rt) + (lt * rf) + (lf * rt)
                    else:
                        ways += lf * rf
                
                # XOR
                else:
                    
                    if isTrue:
                        ways += (lt * rf) + (lf * rt)
                    else:
                        ways += (lt * rt) + (lf * rf)
            
            dp[(i, j, isTrue)] = ways
            return ways
        
        return f(0, n - 1, True)

# 3D DP
class Solution:
    def countWays(self, n, s):

        dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]

        def f(i, j, isTrue):

            if i > j:
                return 0

            if i == j:

                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0

            if dp[i][j][isTrue] != -1:
                return dp[i][j][isTrue]

            ways = 0

            for k in range(i + 1, j, 2):

                op = s[k]

                lt = f(i, k - 1, 1)
                lf = f(i, k - 1, 0)

                rt = f(k + 1, j, 1)
                rf = f(k + 1, j, 0)

                if op == '&':

                    if isTrue:
                        ways += lt * rt
                    else:
                        ways += lt * rf + lf * rt + lf * rf

                elif op == '|':

                    if isTrue:
                        ways += lt * rt + lt * rf + lf * rt
                    else:
                        ways += lf * rf

                else:  # ^

                    if isTrue:
                        ways += lt * rf + lf * rt
                    else:
                        ways += lt * rt + lf * rf

            dp[i][j][isTrue] = ways
            return ways


# Tbaualtaion..
class Solution:
    def countWays(self, n, s):

        dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]

        # base case
        for i in range(0, n, 2):

            if s[i] == 'T':
                dp[i][i][1] = 1
                dp[i][i][0] = 0
            else:
                dp[i][i][1] = 0
                dp[i][i][0] = 1

        # length of expression
        for length in range(3, n + 1, 2):

            for i in range(n - length + 1):

                j = i + length - 1

                for isTrue in range(2):

                    ways = 0

                    # partition at operators
                    for k in range(i + 1, j, 2):

                        op = s[k]

                        lt = dp[i][k - 1][1]
                        lf = dp[i][k - 1][0]

                        rt = dp[k + 1][j][1]
                        rf = dp[k + 1][j][0]

                        # AND
                        if op == '&':

                            if isTrue:
                                ways += lt * rt
                            else:
                                ways += lt * rf + lf * rt + lf * rf

                        # OR
                        elif op == '|':

                            if isTrue:
                                ways += lt * rt + lt * rf + lf * rt
                            else:
                                ways += lf * rf

                        # XOR
                        else:

                            if isTrue:
                                ways += lt * rf + lf * rt
                            else:
                                ways += lt * rt + lf * rf

                    dp[i][j][isTrue] = ways

        return dp[0][n - 1][1]
    