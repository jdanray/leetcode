# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution(object):
	def smallestSubsequence(self, text):
		used = {t: False for t in text}
		count = collections.Counter(text)
		res = []
		for t in text:
			count[t] -= 1

			if used[t]:
				continue

			while res and res[-1] > t and count[res[-1]] > 0:
				used[res[-1]] = False
				res.pop()

			res.append(t)
			used[t] = True

		return ''.join(res)
