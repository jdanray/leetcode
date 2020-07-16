# https://leetcode.com/problems/first-bad-version/ 

class Solution(object):
	def firstBadVersion(self, n):
		lo = 1
		hi = n
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if isBadVersion(mid):
				hi = mid
			else:
				lo = mid + 1

		return lo
