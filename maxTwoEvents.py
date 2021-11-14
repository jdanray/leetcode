# https://leetcode.com/problems/two-best-non-overlapping-events/ 

class Solution(object):
	def maxTwoEvents(self, events):
		N = len(events)
		events = sorted(events, key=lambda e: e[1])

		maxVal = [0 for _ in range(N)]
		maxVal[0] = events[0][2]
		for i in range(1, N):
			maxVal[i] = max(maxVal[i - 1], events[i][2])

		res = events[0][2]
		for j in range(1, N):
			left = 0
			right = j - 1
			while left < right:
				mid = (left + right + 1) // 2

				if events[mid][1] < events[j][0]:
					left = mid
				else:
					right = mid - 1

			res = max(res, events[j][2])
			if events[left][1] < events[j][0]:
				res = max(res, maxVal[left] + events[j][2])

		return res
