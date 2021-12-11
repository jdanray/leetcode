# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/ 

class Solution(object):
	def placeWordInCrossword(self, board, word):
		W = len(word)
		M = len(board)
		N = len(board[0])

		def checkRows(word):
			for i in range(M):
				l = 0
				viable = True
				for j in range(N):
					if board[i][j] == '#':
						if viable and l == W:
							return True
						else:
							l = 0
							viable = True
					elif board[i][j] == ' ' or (l < W and word[l] == board[i][j]):
						l += 1
					else:
						viable = False

				if viable and l == W:
					return True

			return False

		def checkCols(word):
			for j in range(N):
				l = 0
				viable = True
				for i in range(M):
					if board[i][j] == '#':
						if viable and l == W:
							return True
						else:
							l = 0
							viable = True
					elif board[i][j] == ' ' or (l < W and word[l] == board[i][j]):
						l += 1
					else:
						viable = False

				if viable and l == W:
					return True

			return False

		return checkRows(word) or checkRows(word[::-1]) or checkCols(word) or checkCols(word[::-1])
