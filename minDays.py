# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/ 

class Solution(object):
	def minDays(self, bloomDay, m, k):
		def condition(value):
			adjs = 0
			bouquets = 0
			for d in bloomDay:
				if d > value:
					adjs = 0
				else:
					adjs += 1
					if adjs >= k:
						adjs = 0
						bouquets += 1
			return bouquets >= m

		if m * k > len(bloomDay):
			return -1

		left = min(bloomDay)
		right = max(bloomDay)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left
