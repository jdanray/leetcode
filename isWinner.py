# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/ 

class Solution(object):
	def isWinner(self, player1, player2):
		def score(hits):
			res = 0
			strike = -1
			for i, h in enumerate(hits):
				if strike != -1 and i - strike <= 2:
					res += (2 * h) 
				else:
					res += h

				if h == 10:
					strike = i

			return res

		s1 = score(player1)
		s2 = score(player2)

		if s1 == s2:
			return 0
		elif s1 > s2:
			return 1
		else:
			return 2
