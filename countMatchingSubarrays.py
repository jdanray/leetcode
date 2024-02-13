# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/ 

class Solution(object):
	def countMatchingSubarrays(self, nums, pattern):
		n = len(nums)
		m = len(pattern)

		res = 0
		for i in range(n - m):
			match = True
			for j in range(i, i + m):
				if pattern[j - i] == 1 and nums[j + 1] <= nums[j]:
					match = False
					break
				elif pattern[j - i] == 0 and nums[j + 1] != nums[j]:
					match = False
					break
				elif pattern[j - i] == -1 and nums[j + 1] >= nums[j]:
					match = False
					break

			if match:
				res += 1

		return res
