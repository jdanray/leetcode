# https://leetcode.com/problems/container-with-most-water/

class Solution:
	def maxArea(self, height):
		m = 0
		i = 0
		j = len(height) - 1
		while i < j:
			m = max(m, min(height[i], height[j]) * (j - i))
			if height[i] > height[j]:
				j -= 1
			else:
				i += 1
		return m
