# https://leetcode.com/problems/bulb-switcher-iii/ 

class Solution(object):
	def numTimesAllBlue(self, light):
		m = 0
		res = 0
		for i, l in enumerate(light):
			m = max(m, l)
			if i == m - 1:
				res += 1
		return res
