# find all occurences of an ele
# [1,2,3,1,1]
# ans=[0,3,4]
def ls(a,t,i=0,ans=[]):
    if i==len(a):
        return ans
    if a[i]==t:
        ans.append(i)
    return ls(a,t,i+1,ans)

a=list(map(int,input("a:").split()))
t=int(input())
print(ls(a,t))