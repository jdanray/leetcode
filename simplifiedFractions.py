# https://leetcode.com/problems/simplified-fractions/

class Solution(object):
	def simplifiedFractions(self, n):
		seen = set()
		res = []
		for den in range(2, n + 1):
			for num in range(1, den):
				f = num / (den * 1.0)
				if f not in seen:
					res.append(str(num) + '/' + str(den))
					seen.add(f)

		return res
