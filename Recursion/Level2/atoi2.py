
class Solution:
    def myAtoi(self, a: str) -> int:
        def atoi(a,i,ans,sign=1):
            if i==len(a):
                return ans*sign
            if a[i]==" " or a[i]=="0":
                return atoi(a,i+1,ans)
            if a[i]=="-":
                if ans==0:
                    return atoi(a,i+1,-1)
                else:
                    return ans

            if ans==-1:
                return atoi(a,i+1,-1*int(a[i]))
            if '0'<=a[i]<='9':
                return atoi(a,i+1,ans*10+int(a[i]))
            else:
                return atoi(a,i+1,ans)

        return atoi(a,0,0)

    
    