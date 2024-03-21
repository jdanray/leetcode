# https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/ 

class Solution(object):
	def minimumRightShifts(self, nums):
		N = len(nums)

		i = 1
		while i < N and nums[i] >= nums[i - 1]:
			i += 1

		if i >= N:
			return 0
		elif nums[-1] > nums[0]:
			return -1

		j = i + 1
		while j < N and nums[j] >= nums[j - 1]:
			j += 1

		if j < N:
			return -1
		else:
			return N - i
