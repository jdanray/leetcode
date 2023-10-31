# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/ 

class Solution(object):
	def findArray(self, pref):
		xor = 0
		res = []
		for p in pref:
			r = xor ^ p
			xor ^= r
			res.append(r)

		return res
