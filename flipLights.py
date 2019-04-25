# https://leetcode.com/problems/bulb-switcher-ii/

class Solution:
	def mask(self, start, n, step):
		return sum(1 << i for i in range(start, n + 1, step))

	def flipLights(self, n, m):
		even = self.mask(2, n, 2)
		odd = self.mask(1, n, 2) 
		threek = self.mask(1, n, 3)
		each = 2 ** (n + 1) - 2
		statuses = {each}
		for i in range(m):
			statuses = {stat ^ each for stat in statuses} | {stat ^ even for stat in statuses} | {stat ^ odd for stat in statuses} | {stat ^ threek for stat in statuses} 
		return statuses
