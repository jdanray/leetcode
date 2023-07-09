# https://leetcode.com/problems/longest-alternating-subarray/ 

class Solution(object):
	def alternatingSubarray(self, nums):
		N = len(nums)

		res = -1
		for i in range(N):
			m = 1
			for j in range(i + 1, N):
				d = nums[j] - nums[j - 1]
				if m % 2 == 1 and d == 1:
					m += 1
				elif m % 2 == 0 and d == -1:
					m += 1
				else:
					break

				res = max(res, m)

		return res
