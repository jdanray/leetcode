# https://leetcode.com/problems/hash-divided-string/ 

class Solution(object):
	def stringHash(self, s, k):
		char2int = {c: i for i, c in enumerate(string.ascii_lowercase)}
		int2char = {i: c for i, c in enumerate(string.ascii_lowercase)}

		v = 0
		res = ''
		for i, c in enumerate(s):
			if i % k == 0:
				v = 0

			v += char2int[c]

			if i % k == k - 1:
				h = v % len(string.ascii_lowercase)
				res += int2char[h]

		return res
