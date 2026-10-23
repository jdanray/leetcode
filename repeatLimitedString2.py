# https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution(object):
	def repeatLimitedString(self, s, rlim):
		charInt = {c: i for i, c in enumerate(string.ascii_lowercase)}

		count = collections.Counter(s)
		pq = [(-charInt[c], count[c]) for c in count]
		heapq.heapify(pq)

		res = ''
		while pq:
			i, n = heapq.heappop(pq)

			res += string.ascii_lowercase[-i] * min(n, rlim)
			n -= min(n, rlim)

			if n > 0 and pq:
				i2, n2 = heapq.heappop(pq)
                
				res += string.ascii_lowercase[-i2]
				n2 -= 1

				if n2 > 0:
					heapq.heappush(pq, (i2, n2))

				heapq.heappush(pq, (i, n))

		return res