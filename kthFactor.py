# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution(object):
	def kthFactor(self, n, k):
		i = 0
		while i < n and k > 0:
			i += 1
			if n % i == 0:
				k -= 1
                
		return i if k == 0 else -1
