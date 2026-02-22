# https://leetcode.com/problems/find-the-score-difference-in-a-game/

class Solution(object):
	def scoreDifference(self, nums):
		active = 0
		points = [0, 0]
		for i, n in enumerate(nums):
			if n % 2 == 1:
				active = 1 - active

			if i % 6 == 5:
				active = 1 - active

			points[active] += n

		return points[0] - points[1]