# https://leetcode.com/problems/reveal-cards-in-increasing-order/

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

# https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution(object):
	def deckRevealedIncreasing(self, deck):
		deck = sorted(deck, reverse=True)
		res = [deck[0]]
		for card in deck[1:]:
			res = [card] + [res[-1]] + res[:-1]
		return res
