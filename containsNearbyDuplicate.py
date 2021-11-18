# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
	def containsNearbyDuplicate(self, nums, k):
		idx = dict()
		for i in range(len(nums)):
			if nums[i] in idx and i - idx[nums[i]] <= k:
				return True
			idx[nums[i]] = i
		return False

class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		count = collections.Counter()
		for i, n in enumerate(nums):
			count[n] += 1

			if i > k:
				count[nums[i - k - 1]] -= 1

			if count[n] > 1:
				return True

		return False 
