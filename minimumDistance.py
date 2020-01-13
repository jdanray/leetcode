# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

class Solution(object):
	def __init__(self):
		self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.loc = {a: [i // 6, i % 6] for i, a in enumerate(self.alpha)}

	def minimumDistance(self, word):
		memo = {}

		def dist(char1, char2):
			xa = self.loc[char1][0]
			ya = self.loc[char1][1]
			xb = self.loc[char2][0]
			yb = self.loc[char2][1]
			return abs(xa - xb) + abs(ya - yb)

		def minDist(i, left, right):
			if i >= len(word):
				return 0

			if (i, left, right) in memo:
				return memo[i, left, right]	

			d1 = dist(left, word[i])
			d2 = dist(right, word[i])

			mind1 = d1 + minDist(i + 1, word[i], right)
			mind2 = d2 + minDist(i + 1, left, word[i])

			memo[i, left, right] = min(mind1, mind2)
			return memo[i, left, right]

		d1 = min(minDist(0, word[0], a) for a in self.alpha)
		d2 = min(minDist(0, a, word[0]) for a in self.alpha)
		return min(d1, d2) 
