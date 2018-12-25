# https://leetcode.com/problems/isomorphic-strings/description/

class Solution(object):
	def isIsomorphic(self, start, term):
		if len(start) != len(term):
			return False

		sd = dict()
		td = dict()
		for i in range(len(start)):
			if start[i] not in sd:
				sd[start[i]] = term[i]
			if term[i] not in td:
				td[term[i]] = start[i]

			if sd[start[i]] != term[i]:
				return False
			if td[term[i]] != start[i]:
				return False
		return True
