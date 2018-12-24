# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
	def numJewelsInStones(self, J, S):
		J = set(J)
		n = 0
		for s in S:
			if s in J:
				n += 1
		return n
