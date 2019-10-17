# https://leetcode.com/problems/word-subsets/

class Solution(object):
	def wordSubsets(self, A, B):
		Bcount = collections.defaultdict(int)
		for b in B:
			bcount = collections.Counter(b)
			for char in string.ascii_lowercase:
				Bcount[char] = max(Bcount[char], bcount[char])

		res = []
		for a in A:	
			acount = collections.Counter(a)
			if all(acount[char] >= Bcount[char] for char in string.ascii_lowercase):
				res.append(a)

		return res
