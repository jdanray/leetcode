# https://leetcode.com/problems/compare-sums-of-bitonic-parts/

class Solution(object):
	def compareBitonicSums(self, nums):
		a = 0
		d = 0
		for i, n in enumerate(nums):
			if i + 1 >= len(nums) or n > nums[i + 1]:
				d += n
				if nums[i - 1] < n:
					a += n
			else:
				a += n

		return 0 if a > d else 1 if d > a else -1