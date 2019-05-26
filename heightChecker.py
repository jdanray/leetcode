# https://leetcode.com/problems/height-checker/ 

class Solution(object):
	def heightChecker(self, heights):
		sheights = sorted(heights)
		return len([i for i, h in enumerate(heights) if h != sheights[i]])
