class Solution(object):
	def gameOfLife(self, board):
		M = len(board)
		N = len(board[0])

		nlives = collections.defaultdict(int)
		neighbors = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]
		for i in range(M):
			for j in range(N):
				live = 0
				for (di, dj) in neighbors:
					k = i + di
					l = j + dj
					if k >= 0 and l >= 0 and k < M and l < N and board[k][l] == 1:
						live += 1

				nlives[i, j] = live

		for i in range(M):
			for j in range(N):
				if board[i][j] == 0 and nlives[i, j] == 3:
					board[i][j] = 1
				elif board[i][j] == 1 and (nlives[i, j] < 2 or nlives[i, j] > 3):
					board[i][j] = 0
