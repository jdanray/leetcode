# https://leetcode.com/problems/find-the-substring-with-maximum-cost/ 

class Solution(object):
	def maximumCostSubstring(self, s, chars, vals):
		value = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
		for i, c in enumerate(chars):
			value[c] = vals[i]

		res = 0
		cur = 0
		for c in s:
			cur = max(0, cur + value[c])
			res = max(res, cur)
            
		return res
