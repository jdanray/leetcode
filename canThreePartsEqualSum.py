# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution(object):
	def canThreePartsEqualSum(self, A):
		total = sum(A)

		if total % 3 != 0:
			return False

		subtot = total // 3
		s = 0
		count = 0
		for a in A:
			s += a
			if s == subtot:
				count += 1
				s = 0
                    
		return count >= 3
