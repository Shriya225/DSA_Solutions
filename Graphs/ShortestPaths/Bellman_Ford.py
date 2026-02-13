# It detects Negative Cycle
class Solution:
    def bellmanFord(self, V, edges, src):
        ans=[(10**8)]*V
        ans[src]=0
        c=False
        for i in range(V):
            for x,y,z in edges:
                # relax edges
                if ans[x]!=(10**8):
                    if ans[x]+z<ans[y]:
                        if i==V-1:
                            return [-1]
                        ans[y]=ans[x]+z
        return ans