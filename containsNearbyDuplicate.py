# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
	def containsNearbyDuplicate(self, nums, k):
		idx = dict()
		for i in range(len(nums)):
			if nums[i] in idx and i - idx[nums[i]] <= k:
				return True
			idx[nums[i]] = i
		return False
