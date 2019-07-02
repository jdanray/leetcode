# https://leetcode.com/problems/distribute-candies-to-people/

class Solution(object):
	def distributeCandies(self, candies, N):
		dist = [0 for _ in range(N)]
		i = 0
		base = 0
		while candies > 0:
			c = min(base + i + 1, candies)
			dist[i] += c
			candies -= c
			i += 1
			if i == N:
				i = 0
				base += N
		return dist

# a simpler version

class Solution(object):
	def distributeCandies(self, candies, N):
		dist = [0 for _ in range(N)]
		i = 0
		while candies > 0:
			c = min(i + 1, candies)
			dist[i % N] += c
			candies -= c
			i += 1
		return dist
