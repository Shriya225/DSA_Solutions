def frequencySort( s: str) -> str:
        d=dict()
        for i in s:
            d[i]=d.get(i,0)+1
        s=sorted(d.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for i in s:
            ans+=i[0]*i[1]
        return ans


# bucket sort
def sortByFreq(s):
        d=dict()
        for i in s:
            d[i]=d.get(i,0)+1
        b=[[]for i in range(len(s)+1)]
        for i in d:
            b[d[i]].append(i)
        ans=""
        for i in range(len(s),-1,-1):
            while b[i]:
                ch=b[i].pop()
                ans+=ch*i
        return ans
s=input("s:")
print(sortByFreq(s))