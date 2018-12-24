# https://leetcode.com/problems/binary-watch

class Solution(object):
	def readBinaryWatch(self, num):
		if num < 0:
			return []

		times = set()
		stack = [[0, 0, num]]
		while stack:
			hour, minute, n = stack.pop()

			if n == 0:
				h = str(hour)
				m = str(minute)
				if minute < 10:
					m = '0' + m
				times.add(h + ':' + m)
				continue

			for i in range(6):
				b = 1 << i

				if minute & b == 0 and minute + b <= 59:
					stack.append([hour, minute + b, n - 1])

				if i <= 3 and hour & b == 0 and hour + b <= 11:
					stack.append([hour + b, minute, n - 1])
                    
		return list(times)
