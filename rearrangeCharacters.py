# https://leetcode.com/problems/rearrange-characters-to-make-target-string/ 

class Solution(object):
	def rearrangeCharacters(self, s, target):
		countS = collections.Counter(s)
		countT = collections.Counter(target)

		res = float('inf')
		for c in countT:
			res = min(res, countS[c] // countT[c])

		return res
