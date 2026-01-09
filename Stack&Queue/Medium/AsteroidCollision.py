
# def Asteroid(a):
#     ans=[]
#     for i in range(len(a)):
#         if a[i]>0:
#             ans.append(a[i])
#         else:
#             f=0
#             while ans and ans[-1]<=abs(a[i]):
#                 if  ans[-1]==abs(a[i]):
#                     f=1
#                     ans.pop()
#                     break
#                 ans.pop()
#             if f==0 and  not ans:
#                 ans.append(a[i])
#     return ans

def Asteroid(a):
    ans=[]
    for i in a:
        isAlive=True
        while ans and ans[-1]>0 and i<0:
            if ans[-1]<abs(i):
                ans.pop()
                continue
            elif ans[-1]==abs(i):
                ans.pop()
            # also break loop when -ve is smaller
            isAlive=False
            break
        if isAlive:
            ans.append(i)
    return ans

a=list(map(int,input("A:").split()))
print(Asteroid(a))