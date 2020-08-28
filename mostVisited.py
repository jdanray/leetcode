# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution(object):
	def mostVisited(self, n, rounds):
		count = collections.Counter()
		m = len(rounds) - 1
		for i in range(m):
			start = rounds[i]
			stop = rounds[i + 1]
			while start != stop:
				count[start] += 1

				start += 1
				if start > n: 
					start = 1

		count[rounds[-1]] += 1
		freq = max(count.values())
		return [r for r in range(1, n + 1) if count[r] == freq]
