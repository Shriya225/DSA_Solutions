# 1048. Longest String Chain
# recuurence rel'n 
# pick or not pic k strategy..

def lsc(a,i,prev):
    if i==len(a):
        return 0
    # not pick
    ans=lsc(a,i+1,prev)
    # pick
    if prev==-1:
        ans=max(ans,1+lsc(a,i+1,i))
    elif (len(a[i])-len(a[prev]))==1:
        m,n=len(a[i])-1,len(a[prev])-1
        f=0
        while m>=0 and n>=0:
            if a[i][m]!=a[prev][n]:
                f+=1
                m-=1
                if f>1:
                    break
            else:
                m-=1
                n-=1
        if f<=1:
            ans=max(ans,1+lsc(a,i+1,i))
    return ans

# memoization....
class Solution:
    def longestStrChain(self, words):

        words.sort(key=len)

        def lsc(a, i, prev, dp):

            if i == len(a):
                return 0

            if dp[i][prev] != -1:
                return dp[i][prev]

            # not pick
            ans = lsc(a, i+1, prev, dp)

            # pick
            if prev == 0:
                ans = max(ans, 1 + lsc(a, i+1, i+1, dp))

            elif (len(a[i]) - len(a[prev-1])) == 1:

                m, n = len(a[i])-1, len(a[prev-1])-1

                f = 0

                while m >= 0 and n >= 0:

                    if a[i][m] != a[prev-1][n]:

                        f += 1
                        m -= 1

                        if f > 1:
                            break

                    else:
                        m -= 1
                        n -= 1

                if f <= 1:
                    ans = max(ans, 1 + lsc(a, i+1, i+1, dp))
            dp[i][prev] = ans
            return ans
        dp = [[-1]*(len(words)+1) for _ in range(len(words))]
        return lsc(words, 0, 0, dp)



# optimal apprach using Ending at index approach...
class Solution:

    def isPred(self, s1, s2):

        # s2 should be exactly one character bigger
        if len(s2) != len(s1) + 1:
            return False

        i = j = 0

        while i < len(s1) and j < len(s2):

            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s1)

    def longestStrChain(self, words):

        words.sort(key=len)

        n = len(words)

        dp = [1] * n

        ans = 1

        for i in range(n):

            for j in range(i):

                if self.isPred(words[j], words[i]):

                    dp[i] = max(dp[i], 1 + dp[j])

            ans = max(ans, dp[i])

        return ans



