# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/ 

class Solution(object):
	def evaluate(self, s, knowledge):
		know = {key: val for key, val in knowledge}

		opened = False
		bracket = ""
		res = ""
		for c in s:
			if c == "(":
				opened = True
			elif c == ")":
				if bracket in know:
					res += know[bracket]
				else:
					res += "?"
				opened = False
				bracket = ""
			elif opened:
				bracket += c
			else:
				res += c

		return res
