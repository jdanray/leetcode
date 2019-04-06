# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
	def numSubarrayProductLessThanK(self, nums, k):
		if k == 0:
			return 0

		count = 0
		prod = 1
		i = 0
		for j in range(len(nums)):
			prod *= nums[j]
			while prod >= k and i < j:
				prod //= nums[i]
				i += 1
			count += j - i + 1
		return count
