# https://leetcode.com/problems/valid-number/

class Solution(object):
	def isNumber(self, s):
		def isNum(s):
			e = s.find('e')
			if e == -1:
				return isInt(s) or isFloat(s)
			else:
				pre = s[:e]
				post = s[e + 1:]
				if post and (post[0] == '-' or post[0] == '+'):
					post = post[1:]
				return (isInt(pre) or isFloat(pre)) and isInt(post)

		def isInt(s):
			return s.isnumeric()

		def isFloat(s):
			d = s.find('.')
			if d == -1:
				return False
			else:
				pre = s[:d]
				post = s[d + 1:]
				return (not pre or isInt(pre)) and (not post or isInt(post)) and (pre or post)

		s = s.strip()
		if s and (s[0] == '-' or s[0] == '+'):
			return isNum(s[1:])
		else:
			return isNum(s)	
