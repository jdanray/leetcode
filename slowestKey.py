# https://leetcode.com/problems/slowest-key/

class Solution(object):
	def slowestKey(self, releaseTimes, keysPressed):
		dur = releaseTimes[0]
		maxdur = releaseTimes[0]
		res = keysPressed[0]
		for i in range(1, len(releaseTimes)):
			dur = releaseTimes[i] - releaseTimes[i - 1]
			if dur > maxdur or (dur == maxdur and keysPressed[i] > res):
				res = keysPressed[i]
				maxdur = dur
		return res
