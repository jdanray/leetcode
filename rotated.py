# https://leetcode.com/problems/rotated-digits/description/

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
