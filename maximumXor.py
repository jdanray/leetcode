# https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

class Solution(object):
	def maximumXor(self, s, t):
		opp = {'0': '1', '1': '0'}

		count = collections.Counter(t)
		xor = ''
		for b in s:
			if count[opp[b]] > 0:
				xor += '1'
				count[opp[b]] -= 1
			else:
				xor += '0'
				count[b] -= 1

		return xor