# https://leetcode.com/problems/fruit-into-baskets/ 

class Solution(object):
	def totalFruit(self, fruits):
		i = 0
		res = 0
		count = collections.Counter()
		for j, n in enumerate(fruits):
			count[n] += 1

			while len(count) > 2:
				f = fruits[i]
				count[f] -= 1
				if count[f] == 0:
					del count[f]
				i += 1

			res = max(res, j - i + 1)

		return res
