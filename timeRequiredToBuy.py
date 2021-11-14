# https://leetcode.com/problems/time-needed-to-buy-tickets/ 

class Solution(object):
	def timeRequiredToBuy(self, tickets, k):
		res = 0
		line = deque([i for i in range(len(tickets))])
		while tickets[k] > 0:
			i = line.popleft()

			tickets[i] -= 1
			res += 1

			if tickets[i] > 0:
				line.append(i)

		return res
