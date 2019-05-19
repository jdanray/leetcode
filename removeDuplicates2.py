# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution(object):
	def removeDuplicates(self, S):
		res = []
		for c in S:
			res.append(c)
			if len(res) >= 2 and res[-1] == res[-2]:
				res.pop()
				res.pop()
                
		return ''.join(res)
