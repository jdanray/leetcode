# https://leetcode.com/contest/weekly-contest-113/problems/largest-time-for-given-digits/

class Solution(object):
	def largestTimeFromDigits(self, A):
		largest = None
		stack = [[[], 0]]
		A = sorted(A, reverse=True)
		while stack:
			time, used = stack.pop()

			if len(time) == len(A):
				if (0 <= time[0] <= 2) and (0 <= time[1] <= 3 if time[0] == 2 else True) and (0 <= time[2] <= 5): 
					largest = time

			for i, n in enumerate(A):
				if (used >> i) & 1 == 0:
					stack.append([time + [n], used + (1 << i)])

		return "{}{}:{}{}".format(*largest) if largest else ""
