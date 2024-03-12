# https://leetcode.com/problems/maximize-happiness-of-selected-children/ 

class Solution(object):
	def maximumHappinessSum(self, happiness, k):
		hap = sorted(happiness, reverse=True)
		res = 0
		for i in range(k):
			res += max(0, hap[i] - i)
		return res
