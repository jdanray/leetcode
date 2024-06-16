# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/ 

class Solution(object):
	def countCompleteDayPairs(self, hours):
		M = 24
		count = collections.Counter()
		res = 0
		for h in hours:
			res += count[-h % M]
			count[h % M] += 1
		return res
