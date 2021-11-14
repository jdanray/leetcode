# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/ 

class Solution(object):
	def peopleIndexes(self, favoriteCompanies):
		for i, fc in enumerate(favoriteCompanies):
			favoriteCompanies[i] = set(fc)

		res = []
		for i, fc1 in enumerate(favoriteCompanies):
			if not any(fc1.issubset(fc2) for j, fc2 in enumerate(favoriteCompanies) if i != j):
				res.append(i)

		return res
