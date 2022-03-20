# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/ 

class Solution(object):
	def halveArray(self, nums):
		s = sum(nums)
		half = float(s) / 2
		nums = [-float(n) for n in nums]
		heapq.heapify(nums)
		res = 0
		while s > half:
			n = heapq.heappop(nums)
			n = abs(n) / 2
			s -= n
			heapq.heappush(nums, -n)
			res += 1

		return res
