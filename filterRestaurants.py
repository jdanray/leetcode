# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/ 

class Solution(object):
	def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
		rank  = {}
		for (i, r, vf, price, dist) in restaurants:
			if (veganFriendly == 0 or vf == 1) and price <= maxPrice and dist <= maxDistance:
				rank[i] = r 

		return sorted(sorted(rank, reverse=True), reverse=True, key=lambda i: rank[i])
