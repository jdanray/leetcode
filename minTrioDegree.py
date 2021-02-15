# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/ 

class Solution(object):
	def minTrioDegree(self, n, edges):
		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[u].add(v)
			graph[v].add(u)

		istrio = lambda x, y, z: y in graph[x] and z in graph[x] and x in graph[y] and z in graph[y] and x in graph[z] and y in graph[z]

		res = -1
		for i in range(1, n + 1):
			for j in range(i + 1, n + 1):
				for k in range(j + 1, n + 1):
					if istrio(i, j, k):
						deg = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6                        
						if res == -1:
							res = deg
						else:
							res = min(res, deg)
                    
		return res
