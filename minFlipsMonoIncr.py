# https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution(object):
	def minFlipsMonoIncr(self, S):
		memo = {}
		def solve(i, ones):
			if i >= len(S):
				return 0

			if (i, ones) not in memo:
				if S[i] == '0' and ones == True:
					memo[i, ones] = 1 + solve(i + 1, ones)
				elif S[i] == '1' and ones == False:
					memo[i, ones] = min(1 + solve(i + 1, ones), solve(i + 1, True))
				else:
					memo[i, ones] = solve(i + 1, ones)
			return memo[i, ones]

		return solve(0, False)

# After I solve a problem, I like to examine other people's solutions to the problem
# The following is a simpler and more efficient solution

class Solution(object):
	def minFlipsMonoIncr(self, S):
		ones = 0
		flips = 0
		for c in S:
			if c == '0':
				if ones > 0:
					flips += 1
			elif c == '1':
				ones += 1

			flips = min(flips, ones)

		return flips
