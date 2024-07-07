# https://leetcode.com/problems/alternating-groups-i/ 

class Solution(object):
	def numberOfAlternatingGroups(self, colors):
		N = len(colors)
		res = 0
		for i in range(N):
			if colors[i] != colors[(i - 1) % N] and colors[i] != colors[(i + 1) % N]:
				res += 1
		return res

class Solution(object):
	def numberOfAlternatingGroups(self, colors):
		N = len(colors)
		return len([i for i in range(N) if colors[i] != colors[(i - 1) % N] and colors[i] != colors[(i + 1) % N]])
