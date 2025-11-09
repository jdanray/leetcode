# https://leetcode.com/problems/count-subarrays-with-majority-element-i/

class Solution(object):
	def countMajoritySubarrays(self, nums, t):
		N = len(nums)

		res = 0
		for i in range(N):
			count = 0
			for j in range(i, N):
				if nums[j] == t:
					count += 1

				if count * 2 > j - i + 1:
					res += 1

		return res