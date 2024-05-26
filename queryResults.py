# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/ 

class Solution(object):
	def queryResults(self, limit, queries):
		color = {}
		count = collections.Counter()
		distinct = 0
		res = []
		for (x, y) in queries:
			if x in color:
				count[color[x]] -= 1
				if count[color[x]] == 0:
					distinct -= 1

			count[y] += 1
			if count[y] == 1:
				distinct += 1

			color[x] = y
			res.append(distinct)

		return res

class Solution(object):
	def queryResults(self, limit, queries):
		color = {}
		count = collections.Counter()
		distinct = 0
		res = []
		for (x, y) in queries:
			if x not in color or color[x] != y:
				if x in color and color[x] != y:
					count[color[x]] -= 1
					if count[color[x]] == 0:
						distinct -= 1

				count[y] += 1
				if count[y] == 1:
					distinct += 1

				color[x] = y

			res.append(distinct)

		return res
