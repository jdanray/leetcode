# https://leetcode.com/problems/count-days-without-meetings/ 

class Solution(object):
	def countDays(self, days, meetings):
		meetings = sorted(meetings, key=lambda m: m[0])
		inters = [meetings[0]]
		for i in range(1, len(meetings)):
			if meetings[i][0] <= inters[-1][1]:
				inters[-1][1] = max(inters[-1][1], meetings[i][1])
			else:
				inters.append(meetings[i])

		return days - sum(f - s + 1 for (s, f) in inters)
