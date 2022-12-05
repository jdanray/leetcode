# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/ 

class Solution(object):
	def dividePlayers(self, skill):
		skill = sorted(skill)
		t = skill[0] + skill[-1]
		res = 0
		i = 0
		j = len(skill) - 1
		while i < j:
			if skill[i] + skill[j] != t:
				return -1
			else:
				res += skill[i] * skill[j]

			i += 1
			j -= 1
 
		return res
