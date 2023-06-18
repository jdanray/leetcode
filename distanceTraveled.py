# https://leetcode.com/problems/total-distance-traveled/

class Solution(object):
	def distanceTraveled(self, mainTank, additionalTank):
		res = 0
		while mainTank > 0:
			if mainTank >= 5:
				res += 50
				mainTank -= 5
                
				if additionalTank > 0:
					mainTank += 1
					additionalTank -= 1
			else:
				res += mainTank * 10
				mainTank = 0

		return res
