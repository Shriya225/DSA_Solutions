# instead of ans,vis,path
#  using 1 state arr
#   0- unvisited
#   1-visiting
#   2-safe

class Solution:
    def safeNodes(self, V, edges):
        g=[[] for i in range(V)]
        for x,y in edges:
            g[x].append(y)
        state=[0]*V

        def dfs(n):
            if state[n]==2:
                return True
            if state[n]==1:
                return False
            state[n]=1
            for i in g[n]:
                if not dfs(i):
                    return False
            state[n]=2
            return True
        return [i for i in range(V) if dfs(i)]
