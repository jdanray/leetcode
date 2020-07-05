# https://leetcode.com/problems/longest-turbulent-subarray/

class Solution(object):
	def maxTurbulenceSize(self, A):
		gtodd = 1
		ltodd = 1
		res = 1
		for k in range(len(A) - 1):
			if k % 2 == 1:
				if A[k] > A[k + 1]:
					gtodd += 1
					ltodd = 1
				elif A[k] < A[k + 1]:
					gtodd = 1
					ltodd += 1
				else:
					gtodd = 1
					ltodd = 1
			else:
				if A[k] > A[k + 1]:
					ltodd += 1
					gtodd = 1
				elif A[k] < A[k + 1]:
					gtodd += 1
					ltodd = 1
				else:
					gtodd = 1
					ltodd = 1
                    
			res = max(res, gtodd, ltodd)
 
		return res
