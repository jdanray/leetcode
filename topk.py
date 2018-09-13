# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution(object):
	def topKFrequent(self, nums, k):
		f = dict()
		for n in nums:
			if n not in f:
				f[n] = 0
			f[n] += 1
		
		m = max(f[n] for n in f)
		a = [[] for _ in range(m + 1)]
		for n in f:
			a[f[n]].append(n)

		r = []
		for i in range(m, 0, -1):
			j = 0
			while j < len(a[i]) and len(r) < k:
				r.append(a[i][j])
				j += 1

		return r
