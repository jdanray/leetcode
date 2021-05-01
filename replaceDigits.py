# https://leetcode.com/problems/replace-all-digits-with-characters/ 

class Solution(object):
	def replaceDigits(self, s):
		alphabet = string.ascii_lowercase
		index = {a: i for i, a in enumerate(alphabet)}
		res = ""
		for i, c in enumerate(s):
			if i % 2 == 0:
				res += c
			else:
				j = index[s[i - 1]]
				res += alphabet[j + int(c) % len(alphabet)]
		return res
