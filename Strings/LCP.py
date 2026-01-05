# 14. Longest Common Prefix
# vertical scanning
def longestCommonPrefix( a) -> str:
        l=len(min(a,key=len))
        ans=""
        for i in range(l):
            x=a[0][i]
            f=1
            for j in range(1,len(a)):
                if a[j][i]!=x:
                    return ans
            ans+=a[0][i]
        return ans

# also sort and look fr prefi math n 1st and last strs.