# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/ 

class Solution(object):
	def findPrefixScore(self, nums):
		m = 0
		c = 0
		res = []
		for n in nums:
			m = max(m, n)
			c += m + n
			res.append(c)

		return res
