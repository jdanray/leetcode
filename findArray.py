# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/ 

class Solution(object):
	def findArray(self, pref):
		res = [pref[0]]
		xor = pref[0]
		for i in range(1, len(pref)):
			r = xor ^ pref[i]
			res.append(r)
			xor ^= r
            
		return res
