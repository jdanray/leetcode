# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution(object):
	def buildArray(self, target, n):
		k = 1
		res = []
		for t in target:
			while k < t:
				res.append("Push")
				res.append("Pop")
				k += 1

			res.append("Push")
			k += 1

		return res

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
