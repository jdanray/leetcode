# https://leetcode.com/problems/find-common-characters/

from collections import Counter

class Solution(object):
	def commonChars(self, A):
		common = Counter(A[0])
		for i in range(1, len(A)):
			count = Counter(A[i])
			for c in common:
				common[c] = min(common[c], count.get(c, 0))

		res = []
		for c in A[0]:
			if common[c] > 0:
				common[c] -= 1
				res.append(c)

		return res
