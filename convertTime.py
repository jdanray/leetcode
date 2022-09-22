# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/ 

class Solution(object):
	def convertTime(self, current, correct):
		a = 60 * int(current[:2]) + int(current[3:])
		b = 60 * int(correct[:2]) + int(correct[3:])

		res = 0
		d = b - a
		for t in [60, 15, 5, 1]:
			res += (d // t)
			d %= t

		return res
