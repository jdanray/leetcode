# https://leetcode.com/problems/can-make-palindrome-from-substring/ 

class Solution(object):
	def canMakePaliQueries(self, s, queries):
		count = [collections.Counter() for _ in range(len(s) + 1)]
		for i in range(1, len(s) + 1):
			for char in string.ascii_lowercase:
				count[i][char] = count[i - 1][char]
			count[i][s[i - 1]] += 1

		res = []
		for (l, r, k) in queries:
			score = sum((count[r + 1][char] - count[l][char]) % 2 for char in string.ascii_lowercase)
			score //= 2
			res.append(score <= k)
 
		return res

"""
After I solve a problem, I like to examine other people's solutions to the problem.

Although the above solution is correct, it is barely fast enough to pass all test cases. The following solution is a slightly modified version of a solution that someone else came up with. Their solution is worth preserving. 

See this page for more information: https://leetcode.com/problems/can-make-palindrome-from-substring/discuss/371999/Python-100-runtime-and-memory
"""

class Solution:
	def canMakePaliQueries(self, s, queries):
		nums = [ord(c) - ord('a') for c in s]
		dp = [0 for _ in range(len(s) + 1)]
		for i in range(1, len(s) + 1):
			dp[i] = dp[i - 1] ^ (1 << nums[i - 1])

		#ones = lambda x: sum((x >> shift) & 1 for shift in range(26))
		ones = lambda x: bin(x).count('1')
		return [ones(dp[r + 1] ^ dp[l]) >> 1 <= k for l, r, k in queries]
