# https://leetcode.com/problems/roman-to-integer/description/

class Solution(object):
	def romanToInt(self, s):
		units = {'I': ['V','X'], 'X': ['L','C'], 'C': ['D','M']}
		vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		i = 0
		num = 0
		while i < len(s):
			if i + 1 < len(s) and s[i] in units and s[i + 1] in units[s[i]]:
				num += vals[s[i + 1]] - vals[s[i]]
				i += 2
			else:
				num += vals[s[i]]
				i += 1
		return num
