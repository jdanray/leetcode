# https://leetcode.com/problems/smallest-stable-index-ii/

class Solution(object):
	def firstStableIndex(self, nums, k):
		N = len(nums)

		mn = [-1 for _ in range(N)]
		for i in range(N - 1, -1, -1):
			if i == N - 1:
				mn[i] = nums[i]
			else:
				mn[i] = min(mn[i + 1], nums[i])

		mx = float('-inf')
		for i, n in enumerate(nums):
			mx = max(mx, n)
			if mx - mn[i] <= k:
				return i

		return -1