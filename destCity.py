# https://leetcode.com/problems/destination-city/

class Solution(object):
	def destCity(self, paths):
		cities = set()
		for (u, v) in paths:
			cities.add(u)
			cities.add(v)

		outgoing = set(u for u, _ in paths)

		return list(cities - outgoing)[0]
