# https://leetcode.com/problems/snake-in-matrix/ 

class Solution(object):
	def finalPositionOfSnake(self, n, commands):
		i = 0
		j = 0
		for c in commands:
			if c == "UP":
				i -= 1
			elif c == "DOWN":
				i += 1
			elif c == "RIGHT":
				j += 1
			elif c == "LEFT":
				j -= 1

		return (i * n) + j
