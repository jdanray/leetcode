# https://leetcode.com/problems/non-decreasing-array/

class Solution:
	def checkPossibility(self, nums):
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				nums1, nums2 = list(nums), list(nums)
				nums1[i] = nums1[i + 1]
				nums2[i + 1] = nums2[i]
				return self.nondecreasing(nums1) or self.nondecreasing(nums2)
		return True

	def nondecreasing(self, nums):
		return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
