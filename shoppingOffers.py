# https://leetcode.com/problems/shopping-offers/

class Solution(object):
	def shoppingOffers(self, price, special, needs):
		memo = dict()

		def helper(needs):
			if sum(needs) == 0:
				return 0

			tn = tuple(needs)
			if tn in memo:
				return memo[tn]
				
			M = sum(price[i] * needs[i] for i in range(len(needs)))

			for s in special:
				if all(needs[i] >= s[i] for i in range(len(needs))):
					newneeds = [needs[i] - s[i] for i in range(len(needs))]
					M = min(M, s[-1] + helper(newneeds))

			memo[tn] = M
			return M

		return helper(needs)
