# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

class Solution(object):
	def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
		land = zip(landStartTime, landDuration)
		water = zip(waterStartTime, waterDuration)

		lend = min([ls + ld for (ls, ld) in land])
		wend = min([ws + wd for (ws, wd) in water])

		lmin = min(wd + max(lend, ws) for (ws, wd) in water)
		wmin = min(ld + max(wend, ls) for (ls, ld) in land)

		return min(lmin, wmin)