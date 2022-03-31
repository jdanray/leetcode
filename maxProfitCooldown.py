# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
	def maxProfit(self, prices):
		memo = {}
		def helper(i, bought):
			if i >= len(prices):
				return 0

			if (i, bought) in memo:
				return memo[i, bought]

			notrans = helper(i + 1, bought)
			if bought:
				memo[i, bought] = max(notrans, helper(i + 2, False) + prices[i])
			else:
				memo[i, bought] = max(notrans, helper(i + 1, True) - prices[i])
			return memo[i, bought]

		return helper(0, False)

class Solution(object):
	def maxProfit(self, prices):
		p0 = 0
		p1 = -prices[0]
		p2 = float('-inf')
		for i in range(1, len(prices)):
			p0, p1, p2 = max(p0, p2), max(p1, p0 - prices[i]), p1 + prices[i]

		return max(p0, p2)

class Solution(object):
	def maxProfit(self, prices):
		rest = 0
		sell = 0
		for i in range(1, len(prices)):
			sell, rest = max(sell + prices[i] - prices[i - 1], rest), max(sell, rest)

		return max(rest, sell)

class Solution(object):
	def maxProfit(self, prices):
		s1 = -prices[0]
		s2 = 0
		s0 = [0,0]
		for p in prices:
			s1 = max(s1, s0[1] - p)
			s2 = max(s2, s1 + p)
			s0 = [s2, s0[0]] 

		return s2

class Solution(object):
	def maxProfit(self, prices):
		has1DoNothing = -prices[0]
		has1Sell = 0
		has0DoNothing = 0
		has0Buy = -prices[0]
		for i in range(1, len(prices)):
			has1DoNothing = max(has1DoNothing, has0Buy)
			has0Buy = -prices[i] + has0DoNothing
			has0DoNothing = max(has0DoNothing, has1Sell)
			has1Sell = prices[i] + has1DoNothing

		return max(has1Sell, has0DoNothing)

class Solution(object):
	def maxProfit(self, prices):
		res = 0
		ownLast = -prices[0]
		notOwnLast = 0
		notOwnLast2 = 0
		for i in range(1, len(prices)):
			own = max(ownLast, notOwnLast2 - prices[i])
			notOwn = max(notOwnLast, ownLast + prices[i])

			res = max(res, own, notOwn)
			ownLast, notOwnLast, notOwnLast2 = own, notOwn, notOwnLast

		return res

class Solution(object):
	def maxProfit(self, prices):
		N = len(prices)

		buy = [0 for _ in range(N)]
		sell = [0 for _ in range(N)]
		buy[0] = -prices[0]
		for i in range(1, N):
			if i == 1:
				buy[i] = max(buy[i - 1], -prices[i])
			else:
				buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
			sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])

		return sell[N - 1]

class Solution(object):
	def maxProfit(self, prices):
		N = len(prices)

		M = [0 for _ in range(N)]
		maxDiff = float('-inf')
		for i in range(N):
			if i < 2:
				maxDiff = max(maxDiff, -prices[i])

			if i == 0:
				M[i] = 0
			elif i == 1:
				M[i] = max(0, prices[1] - prices[0])
			else:
				M[i] = max(M[i - 1], maxDiff + prices[i])
				maxDiff = max(maxDiff, M[i - 2] - prices[i])

		return M[-1]
