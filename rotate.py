# https://leetcode.com/problems/rotate-array/

class Solution:
	def rotate(self, nums, k):
		rot = [None] * len(nums)
		for i, n in enumerate(nums):
			j = (i + k) % len(nums)
			rot[j] = n

		for i, r in enumerate(rot):
			nums[i] = r
