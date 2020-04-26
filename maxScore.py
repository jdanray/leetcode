# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution(object):
	def maxScore(self, s):
		score = sum(1 if c == '1' else 0 for c in s)
		res = 0
		for i in range(len(s) - 1):
			if s[i] == '0':
				score += 1
			else:
				score -= 1
			res = max(res, score)
		return res 

