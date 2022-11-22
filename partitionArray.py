# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/submissions/ 

class Solution(object):
	def partitionArray(self, nums, k):
		nums = sorted(nums)
		mn = -1
		res = 1
		for n in nums:
			if mn == -1:
				mn = n

			if n - mn > k:
				mn = n
				res += 1

		return res
