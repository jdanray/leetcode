# https://leetcode.com/problems/shuffle-string/ 

class Solution(object):
	def restoreString(self, s, indices):
		res = [''] * len(s)
		for i, c in enumerate(s):
			res[indices[i]] = c
            
		return ''.join(res)
