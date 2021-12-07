# https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution(object):
	def findEvenNumbers(self, digits):
		res = set()
		for i, a in enumerate(digits):
			if a % 2 == 1: 
				continue

			for j, b in enumerate(digits):
				if j == i: 
					continue

				for k, c in enumerate(digits):
					if k == i or k == j or c == 0:
						continue

					res.add(100*c + 10*b + a)

		return sorted(res)
