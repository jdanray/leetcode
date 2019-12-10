# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution(object):
	def tictactoe(self, moves):
		N = 3
		
		# build board
		board = [['' for _ in range(N)] for _ in range(N)]
		mark = 'A'
		for (i, j) in moves:
			board[i][j] = mark            
			if mark == 'A':
				mark = 'B'
			else:
				mark = 'A'

		# determine winner
		def winner(mark):
			# check the 3 cols
			if any(all(board[i][j] == mark for i in range(N)) for j in range(N)):
				return mark

			# check the 3 rows
			if any(all(board[i][j] == mark for j in range(N)) for i in range(N)):
				return mark

			# check left diagonal
			if all(board[i][i] == mark for i in range(N)):
				return mark

			# check right diagonal
			if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
				return mark

			return False

		if winner('A'):
			return 'A'
		if winner('B'):
			return 'B'
		if all(all(board[i][j] == 'A' or board[i][j] == 'B' for j in range(N)) for i in range(N)):
			return 'Draw'
		return 'Pending'
