# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/ 

# Use python3 to memoize the backtracking
class Solution(object):
	def validPartition(self, nums):
		N = len(nums)

		@functools.cache
		def helper(i):
			if i >= N:
				return True
			elif i + 1 >= N:
				return False

			if nums[i + 1] == nums[i]:
				if i + 2 < N and nums[i + 2] == nums[i]:
					return helper(i + 2) or helper(i + 3)
				else:
					return helper(i + 2)
			elif nums[i + 1] == nums[i] + 1:
				if i + 2 < N and nums[i + 2] == nums[i + 1] + 1:
					return helper(i + 3)

			return False

		return helper(0)
