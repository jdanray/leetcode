# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/ 

class Solution(object):
	def takeCharacters(self, s, k):
		N = len(s)
		chars = 'abc'

		if k == 0:
			return 0

		count = collections.Counter()
		right = collections.defaultdict(int)
		for i in range(N - 1, -1, -1):
			count[s[i]] += 1
			right[s[i], count[s[i]]] = N - i

		if not all((ch, k) in right for ch in chars):
			return -1

		count = collections.Counter()
		res = max(right[ch, k] for ch in chars)
		for i, c in enumerate(s):
			count[c] += 1

			m = 0
			for ch in chars:
				n = max(0, k - count[ch])
				m = max(m, right[ch, n])

			res = min(res, m + i + 1)

		return res
