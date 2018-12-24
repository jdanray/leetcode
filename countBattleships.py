# https://leetcode.com/problems/battleships-in-a-board/description/

class Solution:
	def countBattleships(self, board):
		nships = 0
		for i in range(len(board)):
			for j in range(len(board[i])):
				if board[i][j] == 'X' and (j <= 0 or board[i][j - 1] == '.') and (i <= 0 or board[i - 1][j] == '.'):
					nships += 1
		return nships
