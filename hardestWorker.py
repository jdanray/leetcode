# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/ 

class Solution(object):
	def hardestWorker(self, n, logs):
		res = 0
		maxTime = 0
		start = 0
		for (id, leave) in logs:
			t = leave - start
			if t > maxTime or (t == maxTime and id < res):
				maxTime = t
				res = id
                
			start = leave

		return res
