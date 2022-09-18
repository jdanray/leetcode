# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/ 

class Solution(object):
	def matchPlayersAndTrainers(self, players, trainers):
		M = len(players)
		N = len(trainers)

		players = sorted(players)
		trainers = sorted(trainers)
		i = 0
		j = 0
		res = 0
		while i < M and j < N:
			if players[i] <= trainers[j]:
				i += 1
				res += 1
                
			j += 1

		return res 
