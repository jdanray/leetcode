# https://leetcode.com/problems/minesweeper/

class Solution(object):
	def updateBoard(self, board, click):
		i, j = click
		if board[i][j] == 'M':
			board[i][j] = 'X'
		elif board[i][j] == 'E':
			nmines = 0
			for k in range(-1, 2):
				for l in range(-1, 2):
					m, n = i + k, j + l
					if m < len(board) and m >= 0 and n < len(board[0]) and n >= 0 and board[m][n] == 'M':
						nmines += 1

			if nmines == 0:
				board[i][j] = 'B'
				for k in range(-1, 2):
					for l in range(-1, 2):
						m, n = i + k, j + l
						if m < len(board) and m >= 0 and n < len(board[0]) and n >= 0:
							self.updateBoard(board, [m, n])
			else:
				board[i][j] = str(nmines)

		return board	
