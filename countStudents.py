# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/ 

class Solution(object):
	def countStudents(self, students, sandwiches):
		students = collections.deque(students)
		sandwiches = collections.deque(sandwiches)

		leave = 0
		while leave < len(students):
			s = students.popleft()

			if s != sandwiches[0]:
				students.append(s)
				leave += 1
			else:
				sandwiches.popleft()
				leave = 0

		return leave
