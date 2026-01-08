# 739. Daily Temperatures
# montonic stk with indices
def dailyTemp(a):
    ans=[0]*len(a)
    stk=[]
    for i in range(len(a)):
        while stk and stk[-1][0]<a[i]:
            x=stk.pop()
            ans[x[1]]=i-x[1]
        stk.append([a[i],i])
    return ans

a=list(map(int,input("A:").split()))
print(dailyTemp(a))



def dailyTemperatures(temperatures):
        res = [0] * len(temperatures)
        stack = []  # indices

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res