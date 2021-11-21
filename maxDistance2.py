# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

# Time: O(N**2)
# Space: O(1)
class Solution(object):
	def maxDistance(self, colors):
		res = 0
		for j in range(len(colors)):
			i = 0
			while i < j and colors[i] == colors[j]:
				i += 1

			res = max(res, j - i)

		return res

# Time: O(N)
# Space: O(1)
class Solution(object):
	def maxDistance(self, colors):
		N = len(colors)

		first = 0 
		second = 0
		while second < N and colors[second] == colors[first]:
			second += 1

		res = second - first
		for i in range(second + 1, N):
			if colors[i] == colors[first]:
				res = max(res, i - second)
			else:
				res = max(res, i - first)

		return res
