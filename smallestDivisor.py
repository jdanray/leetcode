# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution(object):
	def smallestDivisor(self, nums, threshold):
		def condition(value):
			s = 0
			for n in nums:
				s += math.ceil(float(n) / val)
			return s <= threshold

		left, right = 1, max(nums)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left
