# https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

class Solution(object):
	def canEat(self, candiesCount, queries):
		N = len(candiesCount)

		mustEat = [0 for _ in range(N)]
		for i in range(1, N):
			mustEat[i] = mustEat[i - 1] + candiesCount[i -  1]

		res = []
		for (t, day, cap) in queries:
			amt = (day + 1) * cap
			res.append(amt > mustEat[t] and (day + 1) <= mustEat[t] + candiesCount[t])

		return res
