# https://leetcode.com/problems/find-missing-observations/ 

class Solution(object):
	def missingRolls(self, rolls, mean, n):
		MAX = 6
		m = len(rolls)
		remain = (m + n) * mean - sum(rolls)

		if remain < n or remain > MAX * n:
			return []

		res = [0 for _ in range(n)]
		for i in range(n):
			roll = MAX
			while roll * n > remain:
				roll -= 1

			res[i] = roll
			remain -= roll
			n -= 1

		return res

"""
After I solve a problem, I like to study other solutions. I got a good idea from the following solution:

https://leetcode.com/problems/find-missing-observations/discuss/1500155/Java-easy-solution 
"""

class Solution(object):
	def missingRolls(self, rolls, mean, n):
		MAX = 6
		m = len(rolls)
		remain = (m + n) * mean - sum(rolls)

		if remain < n or remain > MAX * n:
			return []

		p = remain // n
		q = remain % n
		res = [0 for _ in range(n)]
		for i in range(n):
			res[i] = p
			if q > 0:
				res[i] += 1
				q -= 1

		return res


# New solution

class Solution(object):
	def missingRolls(self, rolls, mean, n):
		D = 6

		s = (mean * (len(rolls) + n)) - sum(rolls)
		if n > s:
			return []

		res = [1] * n
		s -= n
		for i in range(len(res)):
			if s == 0:
				break

			x = min(D, s + 1)
			res[i] = x			
			s -= (x - 1)

		return res if s == 0 else []
