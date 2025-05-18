# Brute force o(n^2)
def maxSubArr(a):
    maxs=float('-inf')
    for i in range(len(a)):
        s=0
        for j in range(i,len(a)):
            s+=a[j]
            maxs=max(maxs,s)
    print("maxsum",maxs)
a=list(map(int,input("a:").split()))
maxSubArr(a)