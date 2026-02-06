# BFS
# try to color graph using 2 colors
class Solution:
    def isBipartite(self, g):
        v=[-1]*len(g)
        for k in range(len(g)):
            if v[k]==-1:
                q=[k]
                v[k]=1
                while q:
                    x=q.pop(0)
                    ans=0 if v[x]==1 else 1
                    for i in g[x]:
                        if v[i]==v[x]:
                            return False
                        if v[i]==-1:
                            v[i]=ans
                            q.append(i)
        return True

        