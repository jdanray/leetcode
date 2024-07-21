# https://leetcode.com/problems/minimum-length-of-string-after-operations/ 

class Solution(object):
	def minimumLength(self, s):
		count = collections.Counter(s)
		return sum(2 - count[c] % 2 for c in count)

class Solution(object):
	def minimumLength(self, s):
		count = collections.Counter(s)
		res = 0
		for c in count:
			if count[c] % 2 == 0:
				res += 2
			else:
				res += 1
		return res
