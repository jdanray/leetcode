# https://leetcode.com/contest/weekly-contest-113/problems/reveal-cards-in-increasing-order/

class Solution:
	def deckRevealedIncreasing(self, deck):
		n = len(deck)
		deck = sorted(deck)
		res = [-1 for _ in range(n)]
		queue = list(range(n))
		for i in range(n):
			j = queue.pop(0)
			res[j] = deck[i]
			queue and queue.append(queue.pop(0))
		return res
