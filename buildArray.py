# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution(object):
	def buildArray(self, target, n):
		last = target[-1]
		target = set(target)
		res = []
		for i in range(1, last + 1):
			res.append("Push")
			if i not in target:
				res.append("Pop")
                
		return res
