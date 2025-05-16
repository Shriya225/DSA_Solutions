# array will have just positives..
# 523. Continuous Subarray Sum
# o(n)-tc
# o(n)-sc
def checkSubarraySum(a,k):
    prefix={}
    s=0
    for i in range(len(a)):
        s=(s+a[i])%k
        if i!=0 and s==0:
            print(a[:i+1])
        if s in prefix:
            for j in prefix[s]:
                if j!=i-1:
                    print(a[j+1:i+1])
        if s not in prefix:
            prefix[s]=[i]
        else:
            prefix[s].append(i)
    print(prefix,"preix")
a=list(map(int,input("a:").split()))
k=int(input("K:"))
checkSubarraySum(a,k)