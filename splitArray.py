# https://leetcode.com/problems/split-array-largest-sum/

class Solution(object):
	def splitArray(self, nums, m):
		left = max(nums)
		right = sum(nums)
		while left < right:
			mid = left + (right - left) // 2
			d = 1
			s = 0
			for n in nums:
				if s + n > mid:
					d += 1
					s = n
				else:
					s += n

			if d > m:
				left = mid + 1
			else:
				right = mid

		return left
