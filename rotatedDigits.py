# https://leetcode.com/problems/rotated-digits/description/

class Solution(object):
	def rotatedDigits(self, n):
		rot = {}
		rot[0] = 0
		rot[1] = 1
		rot[2] = 5
		rot[5] = 2
		rot[6] = 9
		rot[8] = 8
		rot[9] = 6

		def isGood(u):
			o = u
			i = 1
			r = 0
			while o > 0:
				d = o % 10

				if d not in rot:
					return 0

				r += rot[d] * i

				i *= 10
				o //= 10

			return r != u

		return sum(isGood(u) for u in range(1, n + 1))

class Solution:
	def rotatedDigits(self, N):
		ngoods = 0
		rots = {0: 0, 1: 1, 8: 8, 2: 5, 5: 2, 6: 9, 9: 6}
		for n in range(1, N + 1):
			good = True
			oldn = n
			newn = 0
			k = 1
			while n > 0:
				d = n % 10
				if d not in rots:
					good = False
					break
				newn += k * rots[d]
				k *= 10
				n //= 10 
			if newn == oldn:
				good = False
			if good:
				ngoods += 1 
		return ngoods	
