# https://leetcode.com/problems/largest-3-same-digit-number-in-string/ 

class Solution(object):
	def largestGoodInteger(self, num):
		L = 3

		sub = 1
		prev = ''
		res = ''
		for n in num:
			if n == prev:
				sub += 1
			else:
				sub = 1

			if sub >= L and n > res:
				res = n

			prev = n

		return res * L

class Solution(object):
	def largestGoodInteger(self, num):
		L = 3
		i = 0
		res = ''
		for j in range(len(num)):
			if j - 1 >= 0 and num[j] != num[j - 1]:
				i = j

			if j - i + 1 == L:
				res = max(res, num[j])

		return L * res

class Solution(object):
	def largestGoodInteger(self, num):
		res = ''
		for i in range(len(num) - 2):
			if num[i] == num[i + 1] == num[i + 2]:
				res = max(res, num[i])
		return 3 * res
