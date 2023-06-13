# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/ 

class Solution(object):
	def longestSemiRepetitiveSubstring(self, s):
		pair = False
		i = 0
		res = 1
		for j in range(1, len(s)):
			if s[j] == s[j - 1]:
				while pair:
					i += 1
					if s[i] == s[i - 1]:
						pair = False
				pair = True

			res = max(res, j - i + 1)

		return res

"""
After I solve a problem, I like to study other people's solutions. I found a simpler solution here:

https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/discuss/3622348/Two-pointer-oror-Very-simple-and-easy-to-understand-solution

I translated the C++ code into Python:
"""

class Solution(object):
	def longestSemiRepetitiveSubstring(self, s):
		prev = -1
		i = 0
		res = 1
		for j in range(1, len(s)):
			if s[j] == s[j - 1]:
				if prev != -1:
					i = prev
				prev = j

			res = max(res, j - i + 1)

		return res
