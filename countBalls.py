# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

class Solution(object):
	def countBalls(self, lowLimit, highLimit):
		boxes = collections.Counter()
		for num in range(lowLimit, highLimit + 1):
			ball = 0
			while num > 0:
				b = num % 10
				ball += b
				num //= 10
			boxes[ball] += 1

		return max(boxes.values())
