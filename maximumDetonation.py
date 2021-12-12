# https://leetcode.com/problems/detonate-the-maximum-bombs/ 

class Solution(object):
	def maximumDetonation(self, bombs):
		N = len(bombs)

		def dist(x1, y1, x2, y2): 
			return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

		blastzone = [[] for _ in range(N)]
		for i in range(N):
			x1, y1, radius = bombs[i]
			for j in range(N):
				x2, y2, _ = bombs[j]
				if dist(x1, y1, x2, y2) <= radius:
					blastzone[i].append(j)

		def dfs(bomb):
			visited = set()
			stack = [bomb]
			res = 0
			while stack:
				i = stack.pop()
				for j in blastzone[i]:
					if j not in visited:
						visited.add(j)
						stack.append(j)
						res += 1
			return res

		return max(dfs(i) for i in range(N))
