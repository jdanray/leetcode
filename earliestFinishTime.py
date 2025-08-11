# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

class Solution(object):
	def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
		land = zip(landStartTime, landDuration)
		water = zip(waterStartTime, waterDuration)

		res = float('inf')
		for (ls, ld) in land:
			for (ws, wd) in water:
				res = min(res, wd + max(ls + ld, ws))

		for (ws, wd) in water:
			for (ls, ld) in land:
				res = min(res, ld + max(ws + wd, ls))

		return res