# https://leetcode.com/problems/course-schedule-ii/

class Solution(object):
	def findOrder(self, numCourses, prereqs):
		innodes = [0 for _ in range(numCourses)]
		outnodes = [set() for _ in range(numCourses)]
		for u, v in prereqs:
			innodes[u] += 1
			outnodes[v].add(u)

		sched = []
		stack = [u for u in range(numCourses) if not innodes[u]]
		while stack:
			u = stack.pop()
			sched.append(u)
			for v in outnodes[u]:
				innodes[v] -= 1
				if not innodes[v]:
					stack.append(v)

		return sched if set(innodes) == {0} else []
