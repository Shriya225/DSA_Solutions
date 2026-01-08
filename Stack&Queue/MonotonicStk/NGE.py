# # brute force
# # o(n*2)
# def nge(a,b):
#     ans=[]
#     for i in a:
#         f=-1
#         for j in b:
#             if i==j:
#                 f=0
#             if f==0 and j>i:
#                 f=-1
#                 ans.append(j)
#                 break
#         if f!=-1:
#             ans.append(-1)
#     return ans
# a=list(map(int,input("A:").split()))
# b=list(map(int,input("b:").split()))
# print(nge(a,b))


# monotnic stack approach
def nge(a,b):
    ans=[]
    stk=[]
    d=dict()
    for i in b:
        while stk and i>stk[-1]:
            d[stk.pop()]=i
        stk.append(i)
    while stk:
        d[stk.pop()]=-1

    for i in a:
        ans.append(d[i])
    return ans
a=list(map(int,input("A:").split()))
b=list(map(int,input("b:").split()))
print(nge(a,b))