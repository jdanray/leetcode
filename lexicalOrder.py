# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
	def lexicalOrder(self, n):
		result = []
		def order(num):
			if len(result) >= n:
				return True
			if num > 0:
				result.append(num)
			b = num * 10
			for c in range(10):
				newnum = b + c
				if newnum != 0 and newnum <= n:
					order(newnum)
		order(0)
		return result

# cool solution to the "lexicographical numbers" problem from
# http://www.cnblogs.com/grandyang/p/5798275.html

def lexorder(n):
	res = []
	cur = 1
	for _ in range(n):
		res.append(cur)
		if cur * 10 <= n:
			cur *= 10
		else:
			if cur >= n:
				cur //= 10
			cur += 1
			while cur % 10 == 0:
				cur //= 10
	return res

# VERY cool solution from 
# http://bookshadow.com/weblog/2016/08/21/leetcode-lexicographical-numbers/
# this solution is "VERY cool" because it consists of few parts and the logic is clear

class Solution(object):
	def lexicalOrder(self, n):
		result = []
		stack = [1]
		while stack:
			y = stack.pop()
			result.append(y)
			if y < n and y % 10 < 9:
				stack.append(y + 1)
			if y * 10 <= n:
				stack.append(y * 10)
		return result
