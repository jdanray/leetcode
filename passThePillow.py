# https://leetcode.com/problems/pass-the-pillow/ 

class Solution(object):
	def passThePillow(self, n, time):
		idx = 1
		d = 1
		for _ in range(time):
			idx += d

			if idx == 1:
				d = 1
			elif idx == n:
				d = -1

		return idx
