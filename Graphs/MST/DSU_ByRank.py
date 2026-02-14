class DSU:
    def __init__(self,v):
        self.p=[i for i in range(v)]
        self.rank=[0]*v
    def find(self, x):
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])  # path compression
            return self.p[x]
    def union(self,u,v):
        x=self.find(u)
        y=self.find(v)
        # if nodes in same set
        if x==y:
            return
        r_x=self.rank[x]
        r_y=self.rank[y]
        if r_x<r_y:
            self.p[x]=y
        elif r_x>r_y:
            self.p[y]=x
        else:
            self.p[x]=y
            self.rank[y]+=1
    

