# https://leetcode.com/problems/count-days-spent-together/

class Solution(object):
	def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
		mlen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		def setDays(arrive, leave):
			m, d = map(int, arrive.split('-'))
			leaveMonth, leaveDay = map(int, leave.split('-'))
			res = set()
			while m <= leaveMonth and (m != leaveMonth or d <= leaveDay):
				res.add((m, d))

				d += 1
				if d > mlen[m - 1]:
					m += 1
					d = 1

			return res

		a = setDays(arriveAlice, leaveAlice)
		b = setDays(arriveBob, leaveBob)

		return len(a & b)
