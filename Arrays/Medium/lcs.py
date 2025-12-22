# 128. Longest Consecutive Sequence

# brute
# def lcs(a):
#     maxele=0
#     ans=0
#     for i in range(len(a)):
#             cnt=0
#             x=a[i]
#             while True:
#                 if x in a:
#                     cnt+=1
#                     ans=max(cnt,ans)
#                     x+=1
#                 else:
#                     break
#     return ans
        
# a=list(map(int,input("a:").split()))
# print(lcs(a))


# optimal
# use set
def lcs(a):
    maxele=0
    ans=0
    s=set(a)
    for i in s:
        if i-1 not in s:
            cnt=0
            x=i
            while x in s:
                cnt+=1
                ans=max(ans,cnt)
                x+=1
    return ans
        
a=list(map(int,input("a:").split()))
print(lcs(a))