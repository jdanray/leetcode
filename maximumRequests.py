# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution(object):
	def maximumRequests(self, n, requests):
		res = 0
		for p in range(1 << len(requests)):
			count = [0 for _ in range(n)]
			transfers = 0
			for i in range(len(requests)):
				if (p >> i) & 1 == 1:
					count[requests[i][0]] += 1
					count[requests[i][1]] -= 1
					transfers += 1

			if count == [0 for _ in range(n)]:
				res = max(res, transfers)

		return res

# The following code is much more memory-efficient, because it uses a while-loop, thereby avoiding the creation of a range object:

class Solution(object):
	def maximumRequests(self, n, requests):
		res = 0
		p = 0
		top = 1 << len(requests)
		while p < top:
			count = [0 for _ in range(n)]
			transfers = 0
			for i in range(len(requests)):
				if (p >> i) & 1 == 1:
					count[requests[i][0]] += 1
					count[requests[i][1]] -= 1
					transfers += 1

			if count == [0 for _ in range(n)]:
				res = max(res, transfers)

			p += 1

		return res
