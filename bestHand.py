# https://leetcode.com/problems/best-poker-hand/ 

class Solution(object):
	def bestHand(self, ranks, suits):
		cr = collections.Counter(ranks)
		cs = collections.Counter(suits)

		if max(cs.values()) == 5:
			return "Flush"
		elif max(cr.values()) >= 3:
			return "Three of a Kind"
		elif max(cr.values()) == 2:
			return "Pair"
		else:
			return "High Card"
