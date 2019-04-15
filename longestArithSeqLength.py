# https://leetcode.com/problems/longest-arithmetic-sequence/

class Solution(object):
	def longestArithSeqLength(self, A):
		longest = 0
		memo = [dict() for _ in range(len(A))]
		for i in range(len(A)):
			for j in range(i):
				step = A[i] - A[j]
				if step in memo[j]:
					memo[i][step] = memo[j][step] + 1
				else:
					memo[i][step] = 2
				longest = max(longest, memo[i][step])
		return longest
