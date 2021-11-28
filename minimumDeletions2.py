# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/ 

class Solution(object):
	def minimumDeletions(self, nums):
		N = len(nums)

		minIdx = min(range(N), key=lambda i: nums[i])
		maxIdx = max(range(N), key=lambda i: nums[i])

		indexes = [min(minIdx, maxIdx), max(minIdx, maxIdx)]

		return min(indexes[1] + 1, N - indexes[0], (indexes[0] + 1) + (N - indexes[1]))
