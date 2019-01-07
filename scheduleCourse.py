# https://leetcode.com/problems/course-schedule-iii/

class Solution(object):
	def scheduleCourse(self, courses):
		courses = sorted(courses, key=lambda c: c[1])
		pq = []
		day = 0
		for c in courses:
			day += c[0]
			heapq.heappush(pq, -c[0])
			if day > c[1]:
				day += heapq.heappop(pq)
		return len(pq)
