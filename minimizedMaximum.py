# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution(object):
	def minimizedMaximum(self, n, quantities):
		def condition(value):
			return sum(ceil(float(q) / value) for q in quantities) <= n

		left = 1 
		right = max(quantities)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left
