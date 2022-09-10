# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/ 

class Solution(object):
	def numberOfWeakCharacters(self, properties):
		properties = sorted(properties, reverse=True)
		gtMax = -1
		eqMax = properties[0][1]
		res = 0
		for i in range(1, len(properties)):
			a, d = properties[i]

			if a == properties[i - 1][0]:
				eqMax = max(eqMax, d)
			else:
				gtMax = max(gtMax, eqMax)
				eqMax = d

			if gtMax > d:
				res += 1

		return res
