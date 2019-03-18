# https://leetcode.com/problems/license-key-formatting/

class Solution(object):
	def licenseKeyFormatting(self, S, K):
		R = ""
		k = K
		i = len(S) - 1
		while i >= 0:
			if k == 0:
				k = K
				R = '-' + R

			if S[i] != '-':
				k -= 1
				R = S[i].upper() + R

			i -= 1

		if R and R[0] == '-':
			R = R[1:]

		return R
