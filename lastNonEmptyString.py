# https://leetcode.com/problems/apply-operations-to-make-string-empty/ 

class Solution(object):
	def lastNonEmptyString(self, s):
		count = collections.Counter(s)
		m = max(count.values())
		res = ''
		for i in range(len(s) - 1, -1, -1):
			if count[s[i]] == m and s[i] not in res: 
				res = s[i] + res
		return res
