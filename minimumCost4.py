# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

"""
There are four possibilities:

(A) Use costBoth for NO need1 and NO need2
(B) Use costBoth for ALL need1 and NO need2
(C) Use costBoth for NO need1 and ALL need2
(D) Use costBoth for ALL need1 and ALL need2

Elaboration:

You either buy no type 3 items, some type 3 items, or only type 3 items. 

If you buy some type 3 items, you buy them in place of either type 1 items or type 2 items.

So, there are four possibilities:

(A) You buy type 1 items to meet need1 and type 2 items to meet need2
(B) You buy type 3 items to meet need1 and type 2 items to meet need2
(C) You buy type 3 items to meet need2 and type 1 items to meet need1
(D) You buy type 3 items to meet need1 and need2

Take the minimum.
"""

class Solution(object):
	def minimumCost(self, cost1, cost2, costBoth, need1, need2):
		a = (cost1 * need1) + (cost2 * need2)
		b = (costBoth * need1) + (cost2 * max(0, need2 - need1))
		c = (costBoth * need2) + (cost1 * max(0, need1 - need2))
		d = costBoth * max(need1, need2)

		return min(a, b, c, d)