# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/ 

class Solution(object):
	def checkTwoChessboards(self, coordinate1, coordinate2):
		def color(coord): 
			return int(coord[1]) % 2 == 1 if ord(coord[0]) % 2 == 1 else int(coord[1]) % 2 == 0

		return color(coordinate1) == color(coordinate2)
