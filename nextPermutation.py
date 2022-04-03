# https://leetcode.com/problems/next-permutation/

class Solution(object):
	def nextPermutation(self, nums):
		N = len(nums)

		i = N - 2
		while i >= 0 and nums[i] >= nums[i + 1]:
			i -= 1

		j = N - 1
		while i >= 0 and j >= 0 and nums[j] <= nums[i]:
			j -= 1

		if i >= 0 and j >= 0:
			nums[i], nums[j] = nums[j], nums[i]

		i += 1
		j = N - 1
		while i < j:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j -= 1
