# https://leetcode.com/problems/maximum-units-on-a-truck/ 

class Solution(object):
	def maximumUnits(self, boxTypes, truckSize):
		res = 0
		boxTypes = sorted(boxTypes, key=lambda b: b[1], reverse=True)
		for (nb, nu) in boxTypes:
			n = min(nb, truckSize)
			truckSize -= n
			res += (n * nu)
			if truckSize == 0: 
				break
		return res
