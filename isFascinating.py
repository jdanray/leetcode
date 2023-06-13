# https://leetcode.com/problems/check-if-the-number-is-fascinating/ 

class Solution(object):
	def isFascinating(self, n):
		n2 = n * 2
		n3 = n * 3

		seen = set()
		while n or n2 or n3:
			d1 = n % 10
			d2 = n2 % 10
			d3 = n3 % 10

			if d1 in seen or d2 in seen or d3 in seen:
				return False
			elif d1 == 0 or d2 == 0 or d3 == 0:
				return False

			seen.add(d1)
			seen.add(d2)
			seen.add(d3)

			n //= 10
			n2 //= 10
			n3 //= 10

		return len(seen) == 9
