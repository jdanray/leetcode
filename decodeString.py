# https://leetcode.com/problems/decode-string/ 

class Solution(object):
	def decodeString(self, s):
		def helper(i, l):
			if i >= l:
				return ""

			if not s[i].isdigit():
				if s[i] == ']':
					return helper(i + 1, l)
				else:
					return s[i] + helper(i + 1, l)

			k = ""
			while s[i].isdigit():
				k += s[i]
				i += 1
			k = int(k)

			j = i + 1
			opened = 1
			while opened > 0:
				if s[j] == '[':
					opened += 1
				elif s[j] == ']':
					opened -= 1
				j += 1

			return (k * helper(i + 1, j)) + helper(j, l)

		return helper(0, len(s))
