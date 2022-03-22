# https://leetcode.com/problems/reorganize-string/ 

class Solution(object):
	def reorganizeString(self, s):
		count = collections.Counter(s)
		res = ""
		pq = [(-count[c], c) for c in count]
		heapq.heapify(pq)
		while pq:
			n1, c1 = heapq.heappop(pq)

			if not pq:
				if n1 == -1:
					return res + c1
				else:
					return ""

			n2, c2 = heapq.heappop(pq)

			res += c1
			res += c2

			n1 += 1
			n2 += 1
			if n1 < 0: heapq.heappush(pq, (n1, c1))
			if n2 < 0: heapq.heappush(pq, (n2, c2))

		return res

"""
After I solve a problem, I like to study other people's solutions. I found a more time- and space-efficient solution here:

https://leetcode.com/problems/reorganize-string/discuss/232469/Java-No-Sort-O(N)-0ms-beat-100

I rewrite that Java program into Python:
"""

class Solution(object):
	def reorganizeString(self, s):
		N = len(s)

		count = collections.Counter(s)
		maxchar = max(count, key=lambda c: count[c])
		if count[maxchar] > (N + 1) / 2:
			return ''

		i = 0
		res = ['' for _ in range(N)]
		while count[maxchar] > 0:
			count[maxchar] -= 1
			res[i] = maxchar
			i += 2

		for c in count:
			while count[c] > 0:
				if i >= N:
					i = 1

				count[c] -= 1
				res[i] = c
				i += 2

		return ''.join(res)
