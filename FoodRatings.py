# https://leetcode.com/problems/design-a-food-rating-system/ 

class FoodRatings(object):
	def __init__(self, foods, cuisines, ratings):
		self.cuisine = {}
		self.cRating = {}
		self.fRating = {}
		for i, c in enumerate(cuisines):
			self.cuisine[foods[i]] = c
			self.fRating[foods[i]] = -ratings[i]

			if c in self.cRating:
				heapq.heappush(self.cRating[c], (-ratings[i], foods[i]))
			else:
				self.cRating[c] = [(-ratings[i], foods[i])]
				heapq.heapify(self.cRating[c])

	def changeRating(self, food, newRating):
		self.fRating[food] = -newRating
		heapq.heappush(self.cRating[self.cuisine[food]], (-newRating, food)) 

	def highestRated(self, cuisine):
		r, f = heapq.heappop(self.cRating[cuisine])
		while self.fRating[f] != r:
			r, f = heapq.heappop(self.cRating[cuisine])

		heapq.heappush(self.cRating[cuisine], (r, f))
		return f
