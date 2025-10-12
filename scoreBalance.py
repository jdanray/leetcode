# https://leetcode.com/problems/equal-score-substrings/

class Solution(object):
	def scoreBalance(self, s):
		score = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}

		tot = sum(score[c] for c in s)
		l = 0
		for c in s:
			l += score[c]
			if l * 2 == tot:
				return True

		return False