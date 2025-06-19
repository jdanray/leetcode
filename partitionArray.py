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

class Solution(object):
	def partitionArray(self, nums, k):
		N = len(nums)
		nums = sorted(nums)
		i = 0
		res = 0
		while i < N:
			res += 1
			start = i
			i += 1
			while i < N and nums[i] - nums[start] <= k:
				i += 1 
		return res
