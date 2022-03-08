# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution(object):
	def mostFrequent(self, nums, key):
		count = collections.Counter()
		for i in range(1, len(nums)):
			if nums[i - 1] == key:
				count[nums[i]] += 1

		return max(count, key=lambda k: count[k])
