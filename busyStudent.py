# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution(object):
	def busyStudent(self, startTime, endTime, queryTime):
		n = 0
		for i, s in enumerate(startTime):
			e = endTime[i]
			if s <= queryTime <= e:
				n += 1
		return n
