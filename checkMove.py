# https://leetcode.com/problems/check-if-move-is-legal/ 

class Solution(object):
	def checkMove(self, board, rMove, cMove, color):
		M = len(board)
		N = len(board[0])
		#assert(M == N == 8)	
		G = 1
	
		inbounds = lambda i, j: i >= 0 and i < M and j >= 0 and j < M

		dirs = []
		dirs.append([-1, 0])	# up
		dirs.append([1, 0])	# down
		dirs.append([0, -1])	# left
		dirs.append([0, 1])	# right
		dirs.append([1, -1])	# southwest (down-left)
		dirs.append([-1, 1])	# northeast (up-right)
		dirs.append([1, 1])	# southeast (down-right)
		dirs.append([-1, -1])	# northwest (up-left)

		for (di, dj) in dirs:
			i = rMove + di
			j = cMove + dj
			nopps = 0
			while inbounds(i, j) and board[i][j] not in [color, '.']:
				nopps += 1
				i += di
				j += dj

			if inbounds(i, j) and board[i][j] == color and nopps >= G:
				return True

		return False
