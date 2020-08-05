# https://leetcode.com/problems/bulls-and-cows/description/ 

class Solution(object):
	def getHint(self, secret, guess):
		cows = 0
		gcount = collections.Counter(guess)
		scount = collections.Counter(secret)
		for g in gcount:
			cows += min(gcount[g], scount[g])

		bulls = 0
		for i in range(len(secret)):
			if secret[i] == guess[i]:
				bulls += 1
				cows -= 1

		return "{}A{}B".format(bulls, cows)

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
