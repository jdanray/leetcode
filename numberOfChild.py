# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/ 

class Solution(object):
	def numberOfChild(self, n, k):
		d = 1
		i = 0
		for _ in range(k):
			i += d

			if i == 0:
				d = 1
			elif i == n - 1:
				d = -1
	
		return i
