# https://leetcode.com/problems/find-in-mountain-array/

class Solution(object):
	def findInMountainArray(self, target, A):
		memo = {}
		def get(idx):
			if idx not in memo:
				memo[idx] = A.get(idx)
			return memo[idx]

		N = A.length()
		lo = 0
		hi = N - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if get(mid) < get(mid + 1):
				lo = mid + 1
			else:
				hi = mid

		peak = lo
		lo = 0
		hi = peak
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if get(mid) == target:
				return mid
			elif get(mid) < target:
				lo = mid + 1
			else:
				hi = mid - 1

		lo = peak
		hi = N - 1
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if get(mid) == target:
				return mid
			elif get(mid) < target:
				hi = mid - 1
			else:
				lo = mid + 1

		return -1
