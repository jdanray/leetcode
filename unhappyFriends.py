# https://leetcode.com/problems/count-unhappy-friends/

class Solution(object):
	def unhappyFriends(self, n, preferences, pairs):
		prefer = [[100000 for _ in range(n)] for _ in range(n)]
		for x, p in enumerate(preferences):
			for i, y in enumerate(p):
				prefer[x][y] = i

		def unhappy(x, y):
			for (u, v) in pairs:
				if prefer[x][u] < prefer[x][y] and prefer[u][x] < prefer[u][v]:
					return True
				elif prefer[x][v] < prefer[x][y] and prefer[v][x] < prefer[v][u]:
					return True

		res = 0
		for (x, y) in pairs:
			if unhappy(x, y):
				res += 1

			if unhappy(y, x):
				res += 1

		return res
