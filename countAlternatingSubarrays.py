# https://leetcode.com/problems/count-alternating-subarrays/ 

class Solution(object):
	def countAlternatingSubarrays(self, nums):
		i = 0
		res = 0
		for j, n in enumerate(nums):
			if j > 0 and nums[j - 1] == n:
				i = j

			res += j - i + 1

		return res
