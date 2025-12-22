# All subsequences
def AllSubseq(a,i=0,ans=[]):
    if i==len(a):
        print(ans)
        return
    ans.append(a[i])
    AllSubseq(a,i+1,ans)
    ans.pop()
    AllSubseq(a,i+1,ans)

a=list(map(int,input("a:").split()))
print(AllSubseq(a))