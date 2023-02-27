# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/ 

class Solution(object):
	def divisibilityArray(self, word, m):
		pre = 0
		res = []
		for d in word:
			pre = (pre * 10 + int(d)) % m

			if pre == 0:
				res.append(1)
			else:
				res.append(0)

		return res
