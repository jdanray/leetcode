# https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution(object):
	def maximumBeauty(self, items, queries):
		items = sorted(items)
		m = 0
		maxBeaut = []
		for (_, b) in items:
			m = max(m, b)
			maxBeaut.append(m)

		prices = sorted([item[0] for item in items])
		res = []
		for q in queries:
			j = bisect.bisect(prices, q)
			if j == len(maxBeaut):
				res.append(maxBeaut[-1])
			elif j - 1 >= 0:
				res.append(maxBeaut[j - 1])
			else:
				res.append(0)

		return res

"""
After I solve a problem, I like to study other people's solutions. I like the idea of this program: https://leetcode.com/problems/most-beautiful-item-for-each-query/discuss/1575898/C%2B%2B-Solution-or-Sorting

The idea: Sort the items--but also sort the queries. Since both items and queries are sorted, if items[i][0] > q, there is no item lte q. While items[i][0] <= q, increment i and find the maximum beauty for all the allowable items.

My code has two for loops. This program only needs one. The nested while loop doesn't make for a quadratic-time algorithm, because i doesn't reset before each iteraton.

Sorting both arrays and considering them both simultaneously, while maintaining a running index for one, is a general idea that can be applied in other contexts.

I have implemented the idea in Python:
"""

class Solution(object):
	def maximumBeauty(self, items, queries):
		items = sorted(items)
		i = 0
		m = 0
		sortedQueries = sorted((q, j) for j, q in enumerate(queries))
		res = [0 for _ in range(len(queries))]
		for (q, j) in sortedQueries:
			while i < len(items) and items[i][0] <= q:
				m = max(m, items[i][1])
				i += 1
			res[j] = m
		return res