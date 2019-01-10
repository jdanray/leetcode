# https://leetcode.com/problems/candy/

class Solution(object):
	def candy(self, ratings):
		candies = [1] * len(ratings)

		for i in range(1, len(ratings)):
			if ratings[i] > ratings[i - 1]:
				candies[i] = candies[i - 1] + 1

		for i in range(1, len(ratings))[::-1]:
			if ratings[i] < ratings[i - 1]:
				candies[i - 1] = max(candies[i] + 1, candies[i - 1])

		return sum(candies)
