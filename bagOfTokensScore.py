# https://leetcode.com/problems/bag-of-tokens/

class Solution(object):
	def bagOfTokensScore(self, tokens, P):
		maxscore = 0
		score = 0
		tokens = sorted(tokens)
		i = 0
		j = len(tokens) - 1
		while i <= j and (P >= tokens[i] or score > 0):
			if P >= tokens[i]:
				P -= tokens[i]
				score += 1
				i += 1
			elif score > 0:
				P += tokens[j]
				score -= 1
				j -= 1
			maxscore = max(maxscore, score)
		return maxscore
