# https://leetcode.com/problems/alphabet-board-path/

class Solution(object):
	def alphabetBoardPath(self, target):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		loc = {a: [i // 5, i % 5] for i, a in enumerate(alphabet)}
		moves  = ''
		pos = [0, 0]
		for c in target:
			lc = loc[c]
			while pos != lc:
				if pos[0] < lc[0] and (pos[0] != 4 or pos[1] == 0):
					pos[0] += 1
					moves += 'D'
				elif pos[0] > lc[0]:
					pos[0] -= 1
					moves += 'U'
				elif pos[1] < lc[1] and pos[0] != 5:
					pos[1] += 1
					moves += 'R'
				else:
					pos[1] -= 1
					moves += 'L'
			moves += '!'
		return moves
