# https://leetcode.com/problems/find-players-with-zero-or-one-losses/  

class Solution(object):
	def findWinners(self, matches):
		losses = collections.Counter()
		players = set()
		for (w, l) in matches:
			losses[l] += 1
			players.add(w)
			players.add(l)

		noLosses = []
		oneLosses = []
		for p in players:
			if losses[p] == 0:
				noLosses.append(p)
			elif losses[p] == 1:
				oneLosses.append(p)

		return [sorted(noLosses), sorted(oneLosses)]
