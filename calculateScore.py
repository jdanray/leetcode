# https://leetcode.com/problems/calculate-score-after-performing-instructions/

class Solution(object):
	def calculateScore(self, instruct, values):
		seen = set()
		i = 0
		res = 0
		while i >= 0 and i < len(instruct) and i not in seen:
			seen.add(i)
            
			if instruct[i] == "add":
				res += values[i]
				i += 1
			elif instruct[i] == "jump":
				i += values[i]

		return res