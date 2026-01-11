# https://leetcode.com/problems/number-of-centered-subarrays/

class Solution(object):
	def centeredSubarrays(self, nums):
		res = 0
		for i in range(len(nums)):
			seen = set()
			s = 0
			for j in range(i, -1, -1):
				seen.add(nums[j])
				s += nums[j]

				if s in seen:
					res += 1

		return res