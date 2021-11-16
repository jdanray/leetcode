# https://leetcode.com/problems/sliding-puzzle/ 

class Solution(object):
	def slidingPuzzle(self, board):
		M = 2
		N = 3
		GOAL = ((1, 2, 3), (4, 5, 0))

		board = (tuple(board[0]), tuple(board[1]))

		zero = -1
		for i in range(M):
			for j in range(N):
				if board[i][j] == 0:
					zero = (i, j)
					break

		seen = set()
		queue = deque([[board, zero, 0]])
		while queue:
			board, zero, moves = queue.popleft()

			if board == GOAL:
				return moves

			zi, zj = zero
			for (di, dj) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
				if zi + di >= M or zi + di < 0 or zj + dj >= N or zj + dj < 0:
					continue

				newBoard = (list(board[0]), list(board[1]))
				newBoard[zi][zj], newBoard[zi + di][zj + dj] = newBoard[zi + di][zj + dj], newBoard[zi][zj]
				newBoard = (tuple(newBoard[0]), tuple(newBoard[1]))

				if newBoard not in seen:
					queue.append([newBoard, (zi + di, zj + dj), moves + 1])
					seen.add(newBoard)

		return -1 
