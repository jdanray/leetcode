# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/ 

class Solution(object):
	def maxUniqueSplit(self, s):
		def helper(i, subs):
			m = 0
			sub = ''
			for j in range(i, len(s)):
				sub += s[j]
				if sub not in subs:
					m = max(m, helper(j + 1, subs | {sub}) + 1)
			return m

		return helper(0, set())
