# https://leetcode.com/problems/longest-nice-substring/

class Solution(object):
	def longestNiceSubstring(self, s):
		N = len(s)

		match = collections.defaultdict(str)
		for i, l in enumerate(string.ascii_lowercase):
			u = string.ascii_uppercase[i]
			match[l] = u
			match[u] = l

		res = ""
		for i in range(N):
			sub = ""
			seen = set()
			missing = 0
			for j in range(i, N):
				sub += s[j]

				if s[j] not in seen:
					if match[s[j]] in seen:
						missing -= 1
					else:
						missing += 1

				if missing == 0 and len(sub) > len(res):
					res = sub

				seen.add(s[j])

		return res
