# ADJ LIST
# SC- O(V+E)
def CreateGraph1(v,e):
    g=[[] for _ in range(v)]
    print(e,g)
    for i in range(len(e)):
        g[e[i][0]].append(e[i][1])
        g[e[i][1]].append(e[i][0])
    return g

v=int(input("v:"))
e=int(input("E:"))
e_l=[]
for _ in range(e):
    e_l.append(list(map(int,input("e_l").split())))
print(CreateGraph1(v,e_l))


# ADJ MATRIX
# SC- O(V^2)
def CreateGraph2(v,e):
    g=[[0]*v for _ in range(v)]
    print(e,g)
    for u,v in e:
        g[u][v]=1
        g[v][u]=1
    return g

v=int(input("v:"))
e=int(input("E:"))
e_l=[]
for _ in range(e):
    e_l.append(list(map(int,input("e_l").split())))
print(CreateGraph2(v,e_l))

