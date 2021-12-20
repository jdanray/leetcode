# https://leetcode.com/problems/adding-spaces-to-a-string/ 

class Solution(object):
	def addSpaces(self, s, spaces):
		j = 0
		res = ""
		for i, c in enumerate(s):
			if j < len(spaces) and i == spaces[j]:
				res += " "
				j += 1
			res += c
		return res
