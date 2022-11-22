# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/submissions/ 

class Solution(object):
	def partitionArray(self, nums, k):
		nums = sorted(nums)
		res = 1
		mn = nums[0]
		for n in nums:
			if n - mn > k:
				res += 1
				mn = n

		return res
