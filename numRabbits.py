# https://leetcode.com/problems/rabbits-in-forest/

class Solution:
	def numRabbits(self, answers):
		num = 0
		count = collections.Counter(answers)
		for n in count:
			num += int(math.ceil(count[n] / (n + 1)) * (n + 1))
		return num

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
