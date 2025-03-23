# https://leetcode.com/problems/maximum-containers-on-a-ship/

class Solution(object):
	def maxContainers(self, n, w, maxWeight):
		return min(maxWeight // w, n * n)