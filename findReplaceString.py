# https://leetcode.com/problems/find-and-replace-in-string/ 

class Solution(object):
	def findReplaceString(self, S, indexes, sources, targets):
		idx = sorted(range(len(indexes)), key=lambda x: indexes[x])
		indexes = [indexes[x] for x in idx]
		sources = [sources[x] for x in idx]
		targets = [targets[x] for x in idx]
		i = 0
		j = 0
		res = ''
		while i < len(S):
			if j < len(indexes) and indexes[j] == i:
				k = i
				l = 0
				while k < len(S) and l < len(sources[j]) and S[k] == sources[j][l]:
					k += 1
					l += 1
				if l < len(sources[j]):
					res += S[i]
					i += 1
				else:
					res += targets[j]
					i = k
				j += 1
			else:
				res += S[i]
				i += 1
		return res
