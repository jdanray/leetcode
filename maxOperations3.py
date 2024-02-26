# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/ 

class Solution(object):
	def maxOperations(self, nums):
		@functools.lru_cache(None)
		def dp(i, j, score):
			if i >= j:
				return 0

			res = 0            
			if nums[i] + nums[i + 1] == score:
				res = max(res, 1 + dp(i + 2, j, score))

			if nums[j] + nums[j - 1] == score:
				res = max(res, 1 + dp(i, j - 2, score))

			if nums[i] + nums[j] == score:
				res = max(res, 1 + dp(i + 1, j - 1, score))

			return res

		a = dp(0, len(nums) - 1, nums[0] + nums[1])
		b = dp(0, len(nums) - 1, nums[-1] + nums[-2])
		c = dp(0, len(nums) - 1, nums[0] + nums[-1])

		return max(a, b, c)
