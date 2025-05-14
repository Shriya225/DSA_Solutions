# bruteForce
# o(^2)
def LongestSubArr(a,k):
    for i in range(len(a)):
        s=0
        for j in range(i,len(a)):
            s+=a[j]
            if s==k:
                print("ans1:",a[i:j+1])
            if s>k:
                break
l=list(map(int,input("a:").split()))
k=int(input("K:"))
LongestSubArr(l,k)