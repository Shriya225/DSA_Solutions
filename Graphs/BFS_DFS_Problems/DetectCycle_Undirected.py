# Undirected Graph Cycle (GFG)
# BFS
from collections import deque
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj_l=[[] for _ in range(V)]
		for x,y in edges:
			adj_l[x].append(y)
			adj_l[y].append(x)
		vis=[False]*V
		for n in range(V):
			if not vis[n]:
				q=deque()
				q.append([n,-1])
				vis[n]=True
				while q:
					x,y=q.popleft()
					for i in adj_l[x]:
						if vis[i] and y!=i:
							return True
						elif not vis[i]:
							q.append([i,x])
							vis[i]=True
		return False