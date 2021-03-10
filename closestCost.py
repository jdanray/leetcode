# https://leetcode.com/problems/closest-dessert-cost/

class Solution(object):
	def closestCost(self, baseCosts, toppingCosts, target):
		N = len(toppingCosts)

		stack = []
		for b in baseCosts:
			stack.append((b, 0))

		res = -1
		seen = set()
		while stack:
			cost, used = stack.pop()

			if (cost, used) in seen:
				continue

			seen.add((cost, used))

			if res == -1:
				res = cost
			elif abs(cost - target) < abs(res - target):
				res = cost
			elif abs(cost - target) == abs(res - target) and cost < res:
				res = cost

			if cost >= target:
				continue

			p = 1
			for i in range(N):
				if (used >> p) & 1 == 0:
 					if (used >> (p - 1)) & 1 == 0:
						stack.append((cost + toppingCosts[i], used + (1 << (p - 1))))
					else:
						stack.append((cost + toppingCosts[i], used + (1 << p)))
				p += 2
                
		return res 
