# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/ 

class Solution(object):
	def divideArray(self, nums, k):
		if len(nums) % 3 != 0:
			return []

		heapq.heapify(nums)
		res = []
		while len(nums) >= 3:
			a = heapq.heappop(nums)
			b = heapq.heappop(nums)
			c = heapq.heappop(nums)

			if c - a > k:
				return []

			res.append([a, b, c])

		return res
