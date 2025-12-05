# 8. String to Integer (atoi)
# start for "0-1" ans:0
# start var is used for "   -+123" 
# "  12  3" ans :12 as spaces are not allowed in b/w
class Solution:
    def atoi(self,s,v=0,i=0,sign=1,start=False):
        print (f"atoi({s},{v},{i},{sign})")
        if i!=len(s) and s[i]==" " and not start:
            return self.atoi(s,v,i+1,sign,start)
        if i<len(s) and  start==False and (s[i]=="+" or s[i]=="-"):
            sign=1 if s[i]=="+" else -1
            start=True
            return self.atoi(s,v,i+1,sign,start)
        if i==len(s) or not s[i].isdigit():
            INT_MIN = -2**31
            INT_MAX = 2**31 - 1
            ans=v*sign
            return max(INT_MIN, min(INT_MAX, ans))
        updated_v=v*10+(ord(s[i])-ord('0'))
        start=True
        return self.atoi(s,updated_v,i+1,sign,start)

    def myAtoi(self, s: str) -> int:
        return self.atoi(s)