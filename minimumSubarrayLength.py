# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/ 

class Solution(object):
	def minimumSubarrayLength(self, nums, k):
		N = len(nums)

		res = float('inf')
		for i in range(N):
			OR = 0
			for j in range(i, N):
				OR |= nums[j]
				if OR >= k:
					res = min(res, j - i + 1)
					break

		return -1 if res == float('inf') else res
