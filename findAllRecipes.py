# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/ 

class Solution(object):
	def findAllRecipes(self, recipes, ingredients, supplies):
		recipes = {r: ingredients[i] for i, r in enumerate(recipes)}
		supplies = set(supplies)

		def hasCycle(r, seen, recur):
			seen.add(r)

			if r not in recipes:
				return False

			recur[r] = True
			for ingred in recipes[r]:
				if ingred not in seen:
					if hasCycle(ingred, seen, recur):
						return True
				elif recur[ingred]:
					return True

			recur[r] = False
			return False

		memo = {}
		def canMake(r):
			if r in memo:
				return memo[r]

			for ingred in recipes[r]:
				if ingred not in supplies and not (ingred in recipes and canMake(ingred)):
					memo[r] = False
					return False

			memo[r] = True
			return True

		return [r for r in recipes if not hasCycle(r, set(), collections.defaultdict(bool)) and canMake(r)]
