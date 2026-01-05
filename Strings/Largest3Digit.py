# 2264. Largest 3-Same-Digit Number in String
def largestGoodInteger( s: str) -> str:
        ans=float("-inf")
        x=s[0]
        c=0
        for i in s:
            if i==x:
                c+=1
            else:
                c=1
                x=i
            if c==3:
                print(i,c)
                ans=max(ans,ord(i)-ord("0"))
        return str(ans)*3 if ans!=float("-inf") else ""