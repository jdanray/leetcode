# https://leetcode.com/problems/asteroid-collision/description/

class Solution:
	def asteroidCollision(self, asteroids):
		rest = []
		for ast in asteroids:
			if ast > 0:
				rest.append(ast)
				continue

			while rest and rest[-1] > 0 and rest[-1] < abs(ast):
				rest.pop()

			if not rest or rest[-1] < 0:
				rest.append(ast)
			elif rest[-1] == abs(ast):
				rest.pop() 

		return rest
