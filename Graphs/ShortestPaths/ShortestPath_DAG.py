# do topo sort
# findshortedt path to each noe intopo osrt before reaching it.
from typing import List


class Solution:

    def shortestPath(self, V: int, E: int,edges: List[List[int]]) -> List[int]:
        g=[[] for i in range(V)]
        for x,y,z in edges:
            g[x].append([y,z])
        stk=[]
        v=[False]*V
        def topo_dfs(n):
            v[n]=True
            for x,y in g[n]:
                if not v[x]:
                    topo_dfs(x)
            stk.append(n)
        for i in range(V):
            if not v[i]:
                topo_dfs(i)
        ans=[float('inf')]*V
        ans[0]=0
        while stk:
            y=stk.pop()
            for nei,wt in g[y]:
                sp=ans[y]+wt
                if sp<ans[nei]:
                    ans[nei]=sp
        return [-1 if i==float('inf') else i for i in ans]


        
        