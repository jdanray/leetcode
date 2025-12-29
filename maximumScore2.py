# https://leetcode.com/problems/maximum-score-of-a-split/

class Solution(object):
	def maximumScore(self, nums):
		N = len(nums)

		suffixMin = [0 for _ in range(N)]
		suffixMin[-1] = nums[-1]
		for i in range(N - 2, -1, -1):
			suffixMin[i] = min(nums[i], suffixMin[i + 1])

		prefixSum = 0
		res = float('-inf')
		for i in range(N - 1):
			prefixSum += nums[i]
			score = prefixSum - suffixMin[i + 1]
			res = max(res, score)

		return res