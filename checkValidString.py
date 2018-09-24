# https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution(object):
	def checkValidString(self, s):
		left = {0}
		for c in s:
			if c == ')' and left == {0}:
				return False

			newleft = set()
			for p in left:
				if c == '(':
					newleft.add(p + 1)
				elif c == ')' and p != 0:
					newleft.add(p - 1)
				elif c == '*':
					newleft.add(p)
					newleft.add(p + 1)
					if p != 0:
						newleft.add(p - 1)

			left = newleft

		return 0 in left
