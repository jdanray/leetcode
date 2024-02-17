# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

class Solution(object):
	def incremovableSubarrayCount(self, nums):
		N = len(nums)

		# For each i, find all j such that nums[i:j+1] is incremovable
		res = 0
		for i in range(N):
			for j in range(i, N):
				# test whether nums[i - 1] < nums[j + 1]
				if i - 1 >= 0 and j + 1 < N and nums[i - 1] >= nums[j + 1]:
					continue

				# test whether nums[:i] is strictly increasing
				if any(nums[k] >= nums[k + 1] for k in range(i - 1)):
					continue

				# test whether nums[j + 1:] is strictly increasing
				if any(nums[k] >= nums[k + 1] for k in range(j + 1, N - 1)):
					continue

				res += 1

		return res
