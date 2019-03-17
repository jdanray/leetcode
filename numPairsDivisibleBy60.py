# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
	def numPairsDivisibleBy60(self, time):
		n = 0
		seen = {}
		for t in time:
			s = -t % 60
			if s in seen:
				n += seen[s]

			m = t % 60
			seen[m] = seen.get(m, 0) + 1

		return n
