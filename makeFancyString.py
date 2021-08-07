# https://leetcode.com/problems/delete-characters-to-make-fancy-string/ 

class Solution(object):
	def makeFancyString(self, s):
		n = 0
		res = ""
		for i, c in enumerate(s):
			if i - 1 >= 0 and s[i - 1] == c:
				n += 1
			else:
				n = 1

			if n < 3:
				res += c

		return res
