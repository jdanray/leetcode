# https://leetcode.com/problems/destroying-asteroids/ 

class Solution(object):
	def asteroidsDestroyed(self, mass, asteroids):
		asteroids = sorted(asteroids)
		for a in asteroids:
			if a > mass:
				return False
			else:
				mass += a

		return True

