# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/ 

class Solution(object):
	def maximumGroups(self, grades):
		i = 0
		res = 0
		while i + res < len(grades):
			res += 1
			i += res

		return res
