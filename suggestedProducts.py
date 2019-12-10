# https://leetcode.com/problems/search-suggestions-system/

class Solution(object):
	def suggestedProducts(self, products, searchWord):
		products = sorted(products)
		pre = ""
		res = []
		for i, c in enumerate(searchWord):
			res.append([])
			pre += c
			for prod in products:
				if i < len(prod) and prod[:i + 1] == pre:
					res[-1].append(prod)

				if len(res[-1]) > 2:
					break

		return res
