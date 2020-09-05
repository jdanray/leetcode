# https://leetcode.com/problems/number-of-ways-to-split-a-string/

class Solution(object):
	def numWays(self, s):
		MOD = 10**9 + 7
		N = len(s)

		nones = s.count('1')

		if nones % 3 != 0:
			return 0

		if nones == 0:
			return sum((N - 2 - i) for i in range(N - 2)) % MOD

		def nzeros(i, d):
			o = 0
			while i < N and o != d:
				if s[i] == '1':
					o += 1
				i += 1

			z = 0
			while i < N and s[i] == '0':
				z += 1
				i += 1

			return z, i

		d = nones // 3
		nzeros1, i = nzeros(0, d)
		nzeros2, _ = nzeros(i, d)

		return ((nzeros1 + 1) * (nzeros2 + 1)) % MOD

"""
After I solve a problem, I like to study other people's solutions. The following program uses the exact same idea as mine, but the implementation is more elegant:

https://leetcode.com/problems/number-of-ways-to-split-a-string/discuss/830455/JavaPython-3-Multiplication-of-the-ways-of-1st-and-2nd-cuts-w-explanation-and-analysis.
"""

class Solution(object):
	def numWays(self, s: str) -> int:
		ones, n = s.count('1'), len(s)
		if ones == 0:
			return (n - 2) * (n - 1) // 2 % (10 ** 9 + 7)
			
		if ones % 3 != 0:
			return 0

		ones //= 3
		count = lo = hi = 0
		for char in s:
			if char == '1':
				count += 1

			if count == ones:
				lo += 1
			elif count == 2 * ones:
				hi += 1

		return lo * hi % (10 **9 + 7)
