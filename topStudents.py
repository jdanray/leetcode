# https://leetcode.com/problems/reward-top-k-students/ 

class Solution(object):
	def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
		pos = set(positive_feedback)
		neg = set(negative_feedback)

		points = collections.Counter()
		for i, rep in enumerate(report):
			s = student_id[i]
			words = rep.split()
			for w in words:
				if w in pos:
					points[s] += 3
				if w in neg:
					points[s] -= 1

		student_id = sorted(student_id)
		res = sorted(student_id, key=lambda s: points[s], reverse=True)[:k]
		return res
