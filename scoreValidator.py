# https://leetcode.com/problems/score-validator/

class Solution(object):
	def scoreValidator(self, events):
		incr = {str(n): [n, 0] for n in range(7)}
		incr["W"] = [0, 1]
		incr["WD"] = [1, 0]
		incr["NB"] = [1, 0]

		res = [0, 0]
		for e in events:
			s, c = incr[e]
            
			res[0] += s
			res[1] += c

			if res[1] == 10:
				return res

		return res