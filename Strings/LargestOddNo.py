# 1903. Largest Odd Number in String
def largestOddNumber(a: str) -> str:
        for i in range(len(a)-1,-1,-1):
            if a[i]!=0 and (ord(a[i])-ord('0'))%2!=0:
                return a[:i+1]
        return ""
        