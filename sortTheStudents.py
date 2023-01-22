# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution(object):
	def sortTheStudents(self, score, k):
		M = len(score)
		N = len(score[0])

		students = list(range(M))
		students = sorted(students, key=lambda i: score[i][k], reverse=True)

		return [[score[i][j] for j in range(N)] for i in students]
