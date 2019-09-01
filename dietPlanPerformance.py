# https://leetcode.com/problems/diet-plan-performance/

class Solution(object):
	def dietPlanPerformance(self, calories, k, lower, upper):
		T = 0
		points = 0
		for i in range(len(calories)):
			T += calories[i]

			if i < k - 1:
				continue
			elif i >= k:
				T -= calories[i - k]

			if T < lower:
				points -= 1
			if T > upper:
				points += 1

		return points

class Solution(object):
	def dietPlanPerformance(self, calories, k, lower, upper):
		T = sum(calories[:k])
		points = 0
		if T < lower:
			points -= 1
		if T > upper:
			points += 1
		
		for i in range(k, len(calories)):
			T += calories[i]
			T -= calories[i - k]
			if T < lower:
				points -= 1
			if T > upper:
				points += 1

		return points
