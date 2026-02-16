# size == no.of nodes in tree.
class DSU:
    def __init__(self,n):
        self.s=[1]*n
        self.p=[i for i in range(n)]
    def findP(self,u):
        if u==self.p[u]:
            return u
        self.p[u]=self.findP(self.p[u])
        return self.p[u]
    def union_BySize(self,u,v):
        x=self.findP(u)
        y=self.findP(v)
        s_x=self.s[x]
        s_y=self.s[y]
        if x!=y:
            if s_x<s_y:
                self.p[x]=y
                self.s[y]+=self.s[x]
            else:
                self.p[y]=x
                self.s[x]+=self.s[y]

