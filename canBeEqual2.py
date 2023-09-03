# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/ 

class Solution(object):
	def canBeEqual(self, s1, s2):
		p1 = {s1, s1[0] + s1[3] + s1[2] + s1[1], s1[2] + s1[1] + s1[0] + s1[3], s1[2] + s1[3] + s1[0] + s1[1]}
		p2 = {s2, s2[0] + s2[3] + s2[2] + s2[1], s2[2] + s2[1] + s2[0] + s2[3], s2[2] + s2[3] + s2[0] + s2[1]}
		return any(p in p2 for p in p1)
