# https://leetcode.com/problems/find-circles/

class Solution:
	def findCircleNum(self, M):
		N = len(M)
		seen = set()

		def dfs(i):
			seen.add(i)
			for j in range(N):
				if M[i][j] == 1 and j not in seen:
					dfs(j)

		ncircles = 0
		for i in range(N):
			if i not in seen:
				dfs(i)
				ncircles += 1

		return ncircles
