# https://leetcode.com/problems/bulls-and-cows/description/ 

class Solution:
	def getHint(self, secret, guess):
		nseen = dict()
		nbulls = 0
		for i in range(min(len(secret), len(guess))):
			s, g = secret[i], guess[i]
			if s == g:
				nbulls += 1
			elif s in nseen:
				nseen[s] += 1
			else:
				nseen[s] = 1

		ncows = 0
		for i, g in enumerate(guess):
			if (i < len(secret) and g != secret[i]) and (g in nseen and nseen[g] > 0):
				nseen[g] -= 1
				ncows += 1

		return '{}A{}B'.format(nbulls, ncows) 
