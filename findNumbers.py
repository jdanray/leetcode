# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

"""
nevens is the "primary" variable. The program return its value. I want to make sure that nevens is up-to-date. How do I do that? What does it mean for nevens to be up-to-date?

1) What does it mean for nevens to be up-to-date? If nevens is up-to-date, then time has passed. State has changed. But nevens has invariantly kept the correct value. What is the correct value for nevens? Say that a number n is "even-digited" if it has an even number of digits. nevens has the correct value if, for each n in nums, nevens is equal to the number of even-digited numbers that we have passed by on the way to n. So, after we pass over all n in nums, nevens is equal to the number of even-digited numbers in nums. And that's what we want to know.

2) How do I keep nevens up-to-date? Initially, nevens == 0, because initially we have seen no n in nums, and thus we have seen zero even-digited numbers. When we arrive at some n in nums, we must inspect it. If n is even-digited, then we increment nevens. If it's not, then we neither increment nor decrement nevens. In either case, we then pass on to the next n in nums. But how do we inspect a given n? [How we do know when n is even-digited?] We create another iteration to find that out. First we create a variable p, and now we keep p up-to-date. So, I imagine that I also have to consider what it means for p to be up-to-date and how to keep p up-to-date.

What does it mean for p to be up-to-date? It means that p is equal to the parity of the number of digits of n seen so far (0->even, 1->odd). Initially, p == 0. We have seen 0 digits of n so far, and 0 is an even number, so we encode p as 0. Now we pass over each digit of n. At each round, we flip the parity. (If p == 0, then we set p to 1. If p == 1, then we set p to 0.) If, at the end of passing over each digit of n, p is equal to 0, then n is an even-digited number, and we know to increment nevens. We can consider each digit of n by dividing n by 10 while n > 0.

This is part of what makes this problem so "easy": The iteration (induction proof) uses a well-known and easy-to-implement technique (ie, dividing a decimal number by 10). Problems that leetcode rates as "medium" and "hard" are more difficult partly because their solutions use less well-known and less easy-to-implement (and less easy-to-understand) techniques. 
"""

class Solution(object):
	def findNumbers(self, nums):
		nevens = 0
		for n in nums:
			p = 0
			while n > 0:
				p = 1 - p
				n //= 10

			if p == 0:
				nevens += 1

		return nevens
