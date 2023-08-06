# https://leetcode.com/problems/account-balance-after-rounded-purchase/ 

class Solution(object):
	def accountBalanceAfterPurchase(self, amt):
		return 100 - ((amt // 10) * 10) - (10 * ((amt % 10) >= 5))
