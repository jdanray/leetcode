# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
	def countArrangement(self, N):
		narrs = 0
		stack = [[1, 0]]
		while stack:
			i, used = stack.pop()

			if i > N:
				narrs += 1
				continue

			for n in range(1, N + 1):
				if (used >> n) & 1 == 0 and (n % i == 0 or i % n == 0):
					stack.append([i + 1, used + (1 << n)])

		return narrs
