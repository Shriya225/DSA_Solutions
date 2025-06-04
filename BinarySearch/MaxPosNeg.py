# Lc-2529. Maximum Count of Positive Integer and Negative Integer
# Given an array nums sorted in non-decreasing order, return the maximum between 
# the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos and the number of 
# negative integers is neg, then return the maximum of pos and neg.

# 0 is not +ve /-ve

# find lower bound of 0 &&  upperbound of 0 which gives no.of 0's
def lowerBound(a,t):
    l=0
    ans=-1
    h=len(a)-1
    # if all ele are less than t,then no ans 
    if a[-1]<t:
        return -1
    # if all ele are > t,ele 0 is ans
    if a[0]>=t:
        return 0
    while l<=h:
        m=(l+h)//2
        if a[m]>=t:
            ans=m
            h=m-1
        else:
            l=m+1
    return ans

def upperBound(a,t):
    l,h=0,len(a)-1
    ans=-1
    while l<=h:
        m=(l+h)//2
        if a[m]>t:
            ans=m
            h=m-1
        else:
            l=m+1
    print("ans:",ans)
    return ans

def maxCount(a,n):
    if a[-1]<0:
        return n
    if a[0]>=1:
        return n
    if a[-1]==0 and a[0]==0:
        return 0
    lb=lowerBound(a,0)
    ub=upperBound(a,0)
    if lb!=-1 and ub==-1:
        return lb
    return max(lb,n-ub)



a=list(map(int,input("a:").split()))
print(maxCount(a,len(a)))