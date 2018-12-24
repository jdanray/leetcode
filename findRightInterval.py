# https://leetcode.com/problems/find-right-interval

class Solution:
	def findRightInterval(self, intervals):
		sortivls = sorted(enumerate(intervals), key=lambda ivl: ivl[1].start)
		res = [-1 for _ in range(len(intervals))]
		for j in range(len(sortivls)):
			i, ivl = sortivls[j]
			idx = self.search(sortivls, ivl, j + 1)
			res[i] = idx
		return res

	def search(self, sortivls, ivl, lo):
		idx = -1
		hi = len(sortivls) - 1
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			i, sivl = sortivls[mid]
			if sivl.start < ivl.end:
				lo = mid + 1
			else:
				hi = mid - 1
				idx = i
		return idx
