# https://leetcode.com/problems/mirror-frequency-distance/

class Solution(object):
	def mirrorFrequency(self, s):
		idx = {c: i for i, c in enumerate(string.ascii_lowercase)}
		freq = collections.Counter(s)

		seen = set()
		res = 0
		for c in s:
			if c in seen:
				continue

			if c.isalpha():
				m = string.ascii_lowercase[-idx[c] - 1]
			else:
				m = str((9 - int(c)) % 10)

			res += abs(freq[c] - freq[m])

			seen.add(c)
			seen.add(m)

		return res