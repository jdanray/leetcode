# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
	def findUnsortedSubarray(self, nums):
		sortednums = sorted(nums)
		left = 0
		right = len(nums) - 1

		while left < len(nums) and nums[left] == sortednums[left]:
			left += 1
		while right > left and nums[right] == sortednums[right]:
			right -= 1

		return right - left + 1

class Solution:
	def findUnsortedSubarray(self, nums):
		sortednums = sorted(nums)
		left = None
		right = 0
		for i in range(len(nums)):
			if nums[i] != sortednums[i]:
				if left == None:
					left = i
				right = i

		return 0 if left == None else right - left + 1
