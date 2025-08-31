# https://leetcode.com/problems/restore-finishing-order/

class Solution(object):
	def recoverOrder(self, order, friends):
		return [o for o in order if o in set(friends)]