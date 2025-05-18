# Kadanes ALgorithm
#  LeetCode 53
def maxSubArr(a):
    maxs=float('-inf')
    s=0
    for i in range(len(a)):
       s+=a[i]
       maxs=max(maxs,s)
       if s<0:
           s=0
    print("maxsum",maxs)
a=list(map(int,input("a:").split()))
maxSubArr(a)