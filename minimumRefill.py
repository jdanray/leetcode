# https://leetcode.com/problems/watering-plants-ii/ 

class Solution(object):
	def minimumRefill(self, plants, capacityA, capacityB):
		res = 0
		capA = capacityA
		capB = capacityB
		i = 0
		j = len(plants) - 1
		while i < j:
			if plants[i] > capA:
				capA = capacityA
				res += 1

			if plants[j] > capB:
				capB = capacityB
				res += 1

			capA -= plants[i]
			capB -= plants[j]

			i += 1
			j -= 1

		if i == j:
			if capA >= capB:
				if plants[i] > capA:
					res += 1
			elif plants[i] > capB:
				res += 1

		return res
