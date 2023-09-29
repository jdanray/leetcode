# https://leetcode.com/problems/monotonic-array/

class Solution(object):
	def isMonotonic(self, nums):
		return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))

class Solution(object):
	def isMonotonic(self, nums):
		if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
			return True
		elif all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)):
			return True
		else:
			return False

class Solution(object):
	def isMonotonic(self, nums):
		N = len(nums)
		inc = 0
		dec = 0
		for i in range(N - 1):
			if nums[i] <= nums[i + 1]:
				inc += 1

			if nums[i] >= nums[i + 1]:
				dec += 1

		return inc == N - 1 or dec == N - 1	
