# https://leetcode.com/problems/partition-labels/description/

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
