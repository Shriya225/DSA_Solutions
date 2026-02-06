# DFS
# Cycle Detection in Undirected Graph
# GFG
class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj_l=[[] for _ in range(V)]
		for x,y in edges:
			adj_l[x].append(y)
			adj_l[y].append(x)
		vis=[False]*V
		def dfs(s,p):
			for i in adj_l[s]:
				if vis[i] and i!=p:
					return True
				if not vis[i]:
					vis[i]=True
					if dfs(i,s):
						return True
			return False
		for i in range(V):
			if not vis[i]:
				vis[i]=True
				if dfs(i,-1):
					return True
		return False