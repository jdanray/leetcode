# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/ 

class Solution(object):
	def checkString(self, s):
		seenB = False
		for c in s:
			if c == 'b':
				seenB = True
			elif seenB:
				return False

		return True

"""
After I solve problems, I like to study other people's solutions. I found a very simple and clever solution here:

https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/discuss/1661056/Python-1-Liner

I wanted to preserve that solution. I translate it (very slightly) from Python3 to Python2 below:
"""

class Solution(object):
	def checkString(self, s):
		return "ba" not in s
