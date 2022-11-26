# https://leetcode.com/problems/word-search/ 

class Solution(object):
	def exist(self, board, word):
		M = len(board)
		N = len(board[0])
		W = len(word)
		deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

		stack = []
		for i in range(M):
			for j in range(N):
				if board[i][j] == word[0]:
					stack.append((i, j, 0, set()))

		while stack:
			i, j, w, seen = stack.pop()

			if w == W - 1:
				return True

			for (di, dj) in deltas:
				k = i + di
				l = j + dj

				if k < 0 or l < 0 or k >= M or l >= N or (k, l) in seen or board[k][l] != word[w + 1]:
					continue

				stack.append((k, l, w + 1, seen | {(i, j)}))

		return False
