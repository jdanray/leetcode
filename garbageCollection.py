# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/ 

class Solution(object):
	def garbageCollection(self, garbage, travel):
		for i in range(1, len(travel)):
			travel[i] += travel[i - 1]

		seen = set()
		res = 0
		for i in range(len(garbage) - 1, -1, -1):
			res += len(garbage[i])

			if i == 0:
				continue

			for g in 'MPG':
				if g not in seen and g in garbage[i]:
					res += travel[i - 1]
					seen.add(g)

		return res
