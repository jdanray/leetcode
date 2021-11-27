# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/ 

class Solution(object):
	def minimumDifference(self, nums, k):
		nums = sorted(nums)
		return min(nums[i] - nums[i - k + 1] for i in range(k - 1, len(nums)))

class Solution(object):
	def minimumDifference(self, nums, k):
		nums = sorted(nums)
		res = float('inf')
		k -= 1
		for i, n in enumerate(nums):
			if i >= k:
				res = min(res, n - nums[i - k])
                
		return res
