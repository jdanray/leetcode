# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/ 

class Solution(object):
	def minOperations(self, nums, k):
		heapq.heapify(nums)
		res = 0
		while len(nums) >= 2 and nums[0] < k:
			x = heapq.heappop(nums)
			y = heapq.heappop(nums)

			heapq.heappush(nums, min(x, y) * 2 + max(x, y))
			res += 1

		return res
