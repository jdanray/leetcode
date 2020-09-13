# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution(object):
	def modifyString(self, s):
		res = ''
		for i, c in enumerate(s):
			if c == '?':
				j = 0
				while (res and res[-1] == string.ascii_lowercase[j]) or (i + 1 < len(s) and s[i + 1] == string.ascii_lowercase[j]):
					j += 1
				res += string.ascii_lowercase[j]
			else:
				res += c
		return res
