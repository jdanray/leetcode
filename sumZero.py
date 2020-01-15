# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

"""
Case 1: n == 0

This is a null case. We must return the empty list.

Case 2: n is even (and n > 0)

For an inductive hypothesis, we assume that sumZero(n - 2) is a list of n - 2 unique integers that sum to 0. How do we extend that solution to cover sumZero(n)? Our procedure is to add both n and -n to the list. The result of this procedure will be a solution for n.

A solution for n must be a list of n unique integers that sum to 0. I will show that the result of the procedure satisfies each of these conditions:

(a) We have n integers:

By hypothesis, sumZero(n - 2) is a list of n - 2 integers. So, when we add both n and -n to that list, we have n integers.

(b) The new list still contains only unique integers:

By hypothesis, sumZero(n - 2) is a list of unique integers. So, I just need to show that n and -n are unique with respect to each other and sumZero(n - 2). Obviously, since n > 0, n != -n. So, the integers aren't duplicates of each other. And neither one of them is a duplicate of any integer in sumZero(n - 2), either. Our procedure is, for each n, to add n and -n to the list. So, since n - 2 < n, neither n nor -n can appear in sumZero(n - 2).

(c) The new list sums to 0:

By hypothesis, sumZero(n - 2) sums to 0. And n + -n == 0. So, we have 0 + 0 == 0.

Case 3: n is odd

We take sumZero(n - 1). Now we have a list of n - 1 unique integers that sum to 0. We extend that solution to cover sumZero(n) by adding 0 to the list. The result of that action will satisfy all the conditions that a solution for n must satisfy:

(a) A solution must consist of n integers:

By hypothesis, sumZero(n - 1) is a list of n - 1 integers. After we add 0 to the list, we have n integers.

(b) The integers must be unique:

By hypothesis, sumZero(n - 1) is a list of unique integers. If we add 0 to the list, it will still contain only unique integers, because 0 doesn't occur in sumZero(n - 1). We show this by case analysis:

(i) In the case where n == 1, 0 doesn't occur in sumZero(n - 1). If n == 1, then sumZero(n - 1) == sumZero(0) == [], which doesn't contain 0.

(ii) In the case where n > 1, n - 1 is an even number that is greater than 0. In that case, sumZero(n - 1) will never contain 0. See Case 2 above.

(c) The integers must sum to 0:

By hypothesis, sumZero(n - 1) sums to 0. If we add 0 to the list, then the list will continue to sum to 0.
"""

class Solution(object):
	def sumZero(self, n):
		if n == 0:
			return []
		elif n % 2 == 0:
			return [n] + [-n] + self.sumZero(n - 2)
		else:
			return [0] + self.sumZero(n - 1)

class Solution(object):
	def sumZero(self, n):
		res = []
		if n % 2 == 1:
			res = [0]
			n -= 1

		for i in range(1, n, 2):
			res.append(-i)
			res.append(i)

		return res
