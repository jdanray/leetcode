# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/ 

class Solution(object):
	def maxDepth(self, s):
		def depth(i, j):
			if i >= j:
				return 0

			if s[i] != '(':
				return depth(i + 1, j)

			p = 0
			start = i
			res = 0
			for k in range(i, j):
				if s[k] == '(':
					p += 1
				elif s[k] == ')':
					p -= 1

				if p == 0:
					res = max(res, 1 + depth(start + 1, k))
					start = k + 1

			return res

		return depth(0, len(s))

"""
After I solve a problem, I like to study other people's solutions. I found a much simpler solution here:

https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/discuss/903258/c%2B%2Bo(n)2-approaches-faster-than-100.00easy-understandinginclude-stack-based

I translate the C++ solution to Python:
"""

class Solution(object):
	def maxDepth(self, s):
		res = 0
		cur = 0
		for c in s:
			if c == '(':
				cur += 1
				res = max(res, cur)
			elif c == ')':
				cur -= 1
		return res
