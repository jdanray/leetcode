# https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution(object):
	def winningPlayerCount(self, n, pick):
		used = collections.defaultdict(bool)
		count = collections.Counter()
		res = 0
		for (p, c) in pick:
			count[p, c] += 1
			if not used[p] and count[p, c] > p:
				used[p] = True
				res += 1
		return res
