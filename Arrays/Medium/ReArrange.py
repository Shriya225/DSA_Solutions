# brute
# o(n) space
# 2149. Rearrange Array Elements by Sign
def rearrange(a):
    pos=[]
    neg=[]
    for i in range(len(a)):
        if a[i]>0:
            pos.append(a[i])
        else:
            neg.append(a[i])
    j=k=0
    for i in range(len(a)):
        if i==0 or i%2==0:
            a[i]=pos[j]
            j+=1
        else:
            a[i]=neg[k]
            k+=1
a=list(map(int,input("a:").split()))
rearrange(a)
print(a)

# 1 pass soln 
# still o(n) space
def rearrangeArray(self, nums):
        pi = 0
        ni = 1
        res = [0] * len(nums)
        
        for n in nums:
            if n > 0:
                res[pi] = n
                pi += 2
            else:
                res[ni] = n
                ni += 2
        
        return res