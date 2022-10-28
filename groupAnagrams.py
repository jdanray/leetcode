# https://leetcode.com/problems/group-anagrams/ 

class Solution(object):
	def groupAnagrams(self, strs):
		alphabet = string.ascii_lowercase
		char2idx = {c: i for i, c in enumerate(alphabet)}

		seen = {}
		m = -1
		res = []
		for s in strs:
			count = [0] * len(alphabet)
			for c in s:
				i = char2idx[c]
				count[i] += 1
			count = tuple(count)

			if count in seen:
				i = seen[count]
				res[i].append(s)
			else:
				m += 1
				seen[count] = m
				res.append([s])

		return res
