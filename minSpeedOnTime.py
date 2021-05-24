# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/ 

class Solution(object):
	def minSpeedOnTime(self, dist, hour):
		MAXHOUR = 10**9

		def condition(speed):
			time = 0
			for d in dist[:-1]:
				time += math.ceil(1.0 * d / speed)
			time += 1.0 * dist[-1] / speed
			return time <= hour

		left = 1
		right = MAXHOUR
		while left < right:
			mid = left + (right - left) // 2
			if condition(mid):
				right = mid
			else:
				left = mid + 1
                
		return left if left < MAXHOUR else -1
