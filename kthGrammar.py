# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
	def kthGrammar(self, N, K):
		grammar = [[1, 0], [0, 1]]
		kth = 0
		for _ in range(N):
			kth = grammar[kth][K % 2]
			K = (K + 1) // 2
		return kth
