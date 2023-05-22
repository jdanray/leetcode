# https://leetcode.com/problems/top-k-frequent-elements/ 

class Solution(object):
	def topKFrequent(self, nums, k):
		freq = collections.Counter(nums)

		m = max(freq.values())
		a = [[] for _ in range(m + 1)]
		for n in freq:
			a[freq[n]].append(n)

		res = []
		for i in range(m, 0, -1):
			j = 0
			while j < len(a[i]) and len(res) < k:
				res.append(a[i][j])
				j += 1

		return res
