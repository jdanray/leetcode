# https://leetcode.com/problems/interval-list-intersections/

class Solution(object):
	def intervalIntersection(self, A, B):
		i = 0
		j = 0
		res = []
		while i < len(A) and j < len(B):
			if (A[i].start <= B[j].end and A[i].end >= B[j].end) or (B[j].start <= A[i].end and B[j].end >= A[i].end):
				inter = Interval(max(A[i].start, B[j].start), min(A[i].end, B[j].end))
				res.append(inter)

			if A[i].end < B[j].end:
				i += 1
			else:
				j += 1

		return res
