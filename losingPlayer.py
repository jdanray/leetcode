# https://leetcode.com/problems/find-the-winning-player-in-coin-game/ 

class Solution(object):
	def losingPlayer(self, x, y):
		X = 1
		Y = 4
		players = ['Bob', 'Alice']
		return players[min(x // X, y // Y) % 2]
