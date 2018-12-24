# https://leetcode.com/problems/positions-of-large-groups/description/

class Solution:
	def largeGroupPositions(self, s):
		l = []
		i = 0
		while i < len(s):
			c = s[i]
			j = i + 1
			while j < len(s) and s[j] == c:
				j += 1
			if j - i >= 3:
				l.append([i, j - 1])
			i = j
		return l
