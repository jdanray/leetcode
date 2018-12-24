# https://leetcode.com/problems/generate-parentheses/description/

# This program doesn't return the result in the order that leetcode likes
# However, the program generates the correct result

"""
def gen_parens(n):
	if n == 0:
		return {''}
	parens = set()
	for p in gen_parens(n - 1):
		parens.add(p + '()')
		parens.add('()' + p)
		parens.add('(' + p + ')')
	return list(parens)
"""

class Solution:
	def generateParenthesis(self, n):
		parens = [set() for _ in range(n + 1)]
		parens[0] = {''}
		for i in range(1, n + 1):
			for p in parens[i - 1]:
				parens[i].add(p + '()')
				parens[i].add('()' + p)
				parens[i].add('(' + p + ')')
		return list(parens[n])

n = 3 
s = Solution()
p = s.generateParenthesis(n)
print(p)
