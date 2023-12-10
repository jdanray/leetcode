# https://leetcode.com/problems/count-tested-devices-after-test-operations/ 

class Solution(object):
	def countTestedDevices(self, battery):
		res = 0
		for b in battery:
			if b - res > 0:
				res += 1
		return res
