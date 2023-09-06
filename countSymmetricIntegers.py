# https://leetcode.com/problems/count-symmetric-integers/ 

class Solution(object):
	def countSymmetricIntegers(self, low, high):
		res = 0
		for x in range(low, high + 1):
			y = x
			l = 0
			while y > 0:
				l += 1
				y //= 10

			if l % 2 == 1:
				continue

			n = l // 2
			s = [0, 0]
			for i in range(l):
				d = x % 10
				s[i < n] += d
				x //= 10

			if s[0] == s[1]:
				res += 1

		return res
