# https://leetcode.com/problems/greatest-sum-divisible-by-three/ 

class Solution(object):
	def maxSumDivThree(self, nums):
		sums = [0, 0, 0]
		for n in nums:
			for s in list(sums):
				j = (s + n) % 3
				sums[j] = max(sums[j], s + n)
		return sums[0]
