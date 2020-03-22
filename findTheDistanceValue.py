# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/ 

class Solution(object):
	def findTheDistanceValue(self, arr1, arr2, d):
		dist = 0
		for n1 in arr1:
			if not any(abs(n1 - n2) <= d for n2 in arr2):
				dist += 1
		return dist
