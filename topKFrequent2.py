# https://leetcode.com/problems/top-k-frequent-words/

class Solution(object):
	def topKFrequent(self, words, k):
		freq = collections.Counter(words)
		
		m = max(freq[w] for w in freq)
		a = [[] for _ in range(m + 1)]
		for w in freq:
			a[freq[w]].append(w)

		res = []
		for i in range(m, 0, -1):
			a[i] = sorted(a[i])
			j = 0
			while j < len(a[i]) and len(res) < k:
				res.append(a[i][j])
				j += 1

		return res
