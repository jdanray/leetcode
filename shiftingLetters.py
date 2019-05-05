# https://leetcode.com/problems/shifting-letters/

class Solution:
	def shiftingLetters(self, S, shifts):
		abc = "abcdefghijklmnopqrstuvwxyz"
		abcidx = {a: i for i, a in enumerate(abc)}
		n = sum(shifts)
		ret = ""
		for i in range(len(shifts)):
			ret += abc[(abcidx[S[i]] + n) % len(abc)]
			n -= shifts[i]
		return ret
