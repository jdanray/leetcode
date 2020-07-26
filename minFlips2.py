# https://leetcode.com/problems/bulb-switcher-iv/

class Solution(object):
	def minFlips(self, target):
		bulb = 0
		res = 0
		for t in target:
			if (bulb == 0 and t == '1') or (bulb == 1 and t == '0'):
				res += 1
				bulb = 1 - bulb
		return res
