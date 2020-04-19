# https://leetcode.com/problems/reformat-the-string/

class Solution(object):
	def reformat(self, s):
		alpha = []
		num = []
		for c in s:
			if c.isalpha():
				alpha.append(c)
			else:
				num.append(c)

		M = len(alpha)
		N = len(num)

		if abs(M - N) > 1:
			return ""

		isalpha = M > N
		res = ""
		while alpha or num:
			if isalpha:
				res += alpha.pop()
			else:
				res += num.pop()
			isalpha = not isalpha
            
		return res
