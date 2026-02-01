# https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

class Solution(object):
	def minimumK(self, nums):
		def condition(k):
			np = sum(math.ceil(1.0 * n / k) for n in nums)
			return np <= k ** 2

		left = 1
		right = nums[-1] * len(nums)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left