# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

class Solution(object):
	def displayTable(self, orders):
		fooditems = sorted({item for (_, _, item) in orders})
		itemnum = {item: i for i, item in enumerate(fooditems)}

		numorders = {}
		for (_, table, item) in orders:
			table = int(table)
			if table not in numorders:
				numorders[table] = collections.defaultdict(int)
			numorders[table][itemnum[item]] += 1

		N = len(fooditems)
		res = [["Table"] + fooditems]
		for table in sorted(numorders.keys()):
			row = [str(table)]
			for item in range(N):
				row.append(str(numorders[table][item]))
			res.append(row)

		return res
