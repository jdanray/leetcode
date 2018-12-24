# https://leetcode.com/problems/h-index-ii/

class Solution(object):
	def hIndex(self, citations):
		N = len(citations)
		lo = 0
		hi = N - 1
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if citations[mid] == N - mid:
				return citations[mid]
			elif citations[mid] > N - mid:
				hi = mid - 1
			else:
				lo = mid + 1
		return N - hi + 1
