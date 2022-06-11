# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/ 

class Solution(object):
	def countSubarrays(self, nums, k):
		res = 0
		s = 0
		i = 0
		for j, c in enumerate(nums):
			s += c

			while (j - i + 1) * s >= k:
				s -= nums[i]
				i += 1

			res += (j - i + 1)

		return res
