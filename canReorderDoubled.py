# https://leetcode.com/contest/weekly-contest-114/problems/array-of-doubled-pairs/

from collections import Counter

class Solution(object):
	def canReorderDoubled(self, A):
		count = Counter(A)
		for a in sorted(A, key=abs):
			if count[a] and count[a * 2]:
				count[a] -= 1
				count[a * 2] -= 1
		return all(count[a] == 0 for a in A)
