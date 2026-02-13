# Minimum Multiplications to reach End
# GFG
# BFS
#User function Template for python3

# mod plays imp role..
# https://chatgpt.com/share/698f03f0-0be4-800d-88f9-d07665e2a4f0
# create a graph
# Expected Time Complexity: O(105)
# Expected Space Complexity: O(105)

from typing import List
 
class Solution:
    
    def minimumMultiplications(self, a : List[int], s : int, e : int) -> int:
        if s==e:
            return 0
        q=[s]
        v=[False]*(100000)
        v[s]=True
        ans=0
        while q:
            n=len(q)
            for i in range(n):
                x=q.pop(0)
                for j in a:
                    y=(x*j)%100000
                    if not v[y]:
                        q.append(y)
                        if y==e:
                            return ans+1
                        v[y]=True
            ans+=1
        return -1
