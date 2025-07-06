# https://leetcode.com/problems/coupon-code-validator/

class Solution(object):
	def validateCoupons(self, code, bus, act):
		cats = ["electronics", "grocery", "pharmacy", "restaurant"]

		def isValid(i):
			return code[i] and act[i] and bus[i] in cats and all(x.isalnum() or x == '_' for x in code[i])

		line = collections.defaultdict(list)
		for i, c in enumerate(code):
			if isValid(i):
				line[bus[i]].append(c)

		res = []
		for b in cats:
			line[b].sort()
			res += line[b]

		return res