# https://leetcode.com/problems/partition-labels/

class Solution(object):
	def partitionLabels(self, s):
		maxLoc = collections.defaultdict(int)
		for i, c in enumerate(s):
			maxLoc[c] = i

		start = 0
		res = []
		while start < len(s):
			i = start
			m = maxLoc[s[start]]
			while i < m:
				m = max(m, maxLoc[s[i]])
				i += 1

			res.append(i - start + 1)
			start = i + 1

		return res

class Solution(object):
	def partitionLabels(self, S):
		maxp = dict()
		for i, c in enumerate(S):
			maxp[c] = i

		nlabels = []
		i = 0
		while i < len(S):
			j = i
			seen = {S[i]}
			m = max(maxp[c] for c in seen)

			while j != m:
				j += 1
				seen.add(S[j])
				m = max(maxp[c] for c in seen)

			nlabels.append(j - i + 1)
			i = j + 1

		return nlabels

class Solution(object):
	def partitionLabels(self, s):
		count = collections.Counter(s)
		i = 0
		res = []
		while i < len(s):
			seen = {s[i]}
			count[s[i]] -= 1
			i += 1

			l = 1
			while any(count[c] > 0 for c in seen):
				seen.add(s[i])
				count[s[i]] -= 1
				i += 1
				l += 1

			res.append(l)

		return res
