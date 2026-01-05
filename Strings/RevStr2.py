# 541. Reverse String II
# brute soln
def reverse(str,i,j,k):
        print(i,j)
        rev=''
        for g in range(i,j+1):
            if g-i<k:
                print(i-g)
                rev=str[g]+rev
            else:
                rev+=str[g]
        return rev

def reverseStr( s: str, k: int) -> str:
        i=j=0
        ans=''
        while j<len(s):
            if (j-i+1)==(k*2):
                ans+=reverse(s,i,j,k)
                print("herer")
                i=j+1
            j+=1
        return ans
s=input("s:")
k=int(input("K:"))
print(reverseStr(s,k))