# https://leetcode.com/problems/odd-string-difference/

class Solution(object):
	def oddString(self, words):
		c2n = {c: n for n, c in enumerate(string.ascii_lowercase)}

		arr = collections.defaultdict(list)
		for w in words:
			d = tuple(c2n[w[j]] - c2n[w[j - 1]] for j in range(1, len(w)))
			arr[d].append(w)

		for d in arr:
			if len(arr[d]) == 1:
				return arr[d][0]
