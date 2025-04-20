# https://leetcode.com/problems/rabbits-in-forest/

class Solution:
	def numRabbits(self, answers):
		nrabbits = 0
		nseen = dict()
		for n in answers:
			if n == 0:
				nrabbits += 1
				continue

			if n not in nseen:
				nseen[n] = 0

			if nseen[n] == 0:
				nrabbits += (n + 1)

			if nseen[n] == n:
				nseen[n] = 0
			else:
				nseen[n] += 1

		return nrabbits
