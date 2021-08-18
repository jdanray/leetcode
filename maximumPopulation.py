# https://leetcode.com/problems/maximum-population-year/

class Solution(object):
	def maximumPopulation(self, logs):
		logs = sorted(logs, key=lambda l: l[0])

		maxpop = 0
		maxyear = -1
		for i, (birthi, deathi) in enumerate(logs):
			pop = 1
			for j in range(i):
				birthj, deathj = logs[j]
				if birthi < deathj and birthi >= birthj:
					pop += 1

			if pop > maxpop:
				maxpop = pop
				maxyear = birthi

		return maxyear

"""
After I solve problems, I like to examine other people's solutions. I found the following solution and translated it into Python: 

https://leetcode.com/problems/maximum-population-year/discuss/1198892/O(n)-Line-Sweep
"""

class Solution(object):
	def maximumPopulation(self, logs):
		pop = collections.defaultdict(int)
		for (birth, death) in logs:
			pop[birth] += 1
			pop[death] -= 1

		res = (0, 0)
		for i in range(1950, 2050 + 1):
			pop[i] += pop[i - 1]
			if pop[i] > res[0]:
				res = (pop[i], i)

		return res[1]
