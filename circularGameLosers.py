# https://leetcode.com/problems/find-the-losers-of-the-circular-game/ 

class Solution(object):
	def circularGameLosers(self, n, k):
		seen = set()
		p = 0
		m = 1
		while p not in seen:
			seen.add(p)           
			p = (p + m * k) % n
			m += 1

		return [p + 1 for p in range(n) if p not in seen]
