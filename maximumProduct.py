# https://leetcode.com/problems/maximum-product-after-k-increments/ 

class Solution(object):
	def maximumProduct(self, nums, k):
		MOD = 10**9 + 7

		heapq.heapify(nums)
		for _ in range(k):
			n = heapq.heappop(nums)
			n += 1
			heapq.heappush(nums, n)

		res = 1
		for n in nums:
			res *= n
			res %= MOD

		return res
