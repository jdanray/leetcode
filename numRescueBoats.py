# https://leetcode.com/problems/boats-to-save-people/

class Solution:
	def numRescueBoats(self, people, limit):
		people = sorted(people)
		i = 0
		j = len(people) - 1
		nboats = 0
		while i <= j:
			if people[i] + people[j] <= limit:
				i += 1
			j -= 1
			nboats += 1
		return nboats
		
