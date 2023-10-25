# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
	def kthGrammar(self, N, K):
		grammar = [[1, 0], [0, 1]]
		kth = 0
		for _ in range(N):
			kth = grammar[kth][K % 2]
			K = (K + 1) // 2
		return kth

class Solution(object):
	def kthGrammar(self, n, k):
		if n == 1:
			return 0

		pre = self.kthGrammar(n - 1, (k - 1) // 2 + 1)
		if pre == 0:
			return 1 - (k % 2)
		else:
			return k % 2

class Solution(object):
	def kthGrammar(self, n, k):
		return 0 if n == 1 else [1 - (k % 2), k % 2][self.kthGrammar(n - 1, (k - 1) // 2 + 1)]
