# https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution(object):
	def countPartitions(self, nums):
		total = sum(nums)
		left = 0
		res = 0
		for i in range(len(nums) - 1):
			left += nums[i]
			right = total - left
			if abs(right - left) % 2 == 0:
				res += 1
		return res