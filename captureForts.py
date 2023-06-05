# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/ 

class Solution(object):
	def captureForts(self, forts):
		z = 0
		res = 0
		for i, f in enumerate(forts):
			if f == 1 or f == -1:
				j = i - 1 - z
				if j >= 0 and forts[j] == -f:
					res = max(res, z)
				z = 0
			elif f == 0:
				z += 1

		return res
