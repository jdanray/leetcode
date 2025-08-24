# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/  

"""
The basic idea for the following program is that deleting an element can increase the length of the longest subarray of 1s only if 

	(1) the element is a 0, and
	(2) there are two subarrays of 1s to the left and right of the 0.

So, for each nums[i], if nums[i] == 0, I want to know the lengths of the subarrays of 1s to the left and right of nums[i] (if there are any). I take two passes through nums in order to determine that information:

-In the first iteration, I create the list lensones: lensones[i] is the length of the subarray of 1s that ends at i.
-On the second iteration, I find the start index j of each subarray of 1s and set lensones[j] to the length of that subarray.

Now, for each nums[i], if nums[i] == 0, I know the lengths of the subarrays of 1s to the left and right of nums[i]. Now you just determine whether removing nums[i] (and thereby conjoining the subarrays to the left and right of nums[i]) will increase the result.

There is one special case: If nums is all 1's, then we must return len(nums) - 1.
"""

class Solution(object):
	def longestSubarray(self, nums):
		N = len(nums)

		ones = 0
		lensones = []
		for n in nums:
			if n == 1:
				ones += 1
			else:
				ones = 0
			lensones.append(ones)

		if ones == N:
			return N - 1

		i = N - 1
		while i > 0:
			if nums[i] == 1:
				j = i - lensones[i]
				lensones[j + 1] = lensones[i]
				i = j 
			else:
				i -= 1

		res = 0
		for i in range(N):
			res = max(res, lensones[i])
			if lensones[i] == 0 and i - 1 >= 0 and i + 1 < N:
				res = max(res, lensones[i - 1] + lensones[i + 1])

		return res

"""
After I solve a problem, I like to examine other people's solutions to the problem.

One leetcoder gives a DP-based solution: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/708109/Python-O(n)-dynamic-programming-detailed-explanation

The basic idea is, for each nums[i], to keep track of

(a) the length of the subarray of only 1s that ends at nums[i]
(b) the length of the subarray of 1s, that contains one 0, that ends at nums[i]

The answer is the maximum of (a) and (b), over all nums[i]. 

Again, there is one special case: If nums is all 1's, then we must return len(nums) - 1.

The linked program uses O(n) space. I reimplemented the basic idea so that it requires just O(1) space: 
"""

class Solution(object):
	def longestSubarray(self, nums):
		N = len(nums)

		allones = 0
		onezero = 0
		res = 0
		for n in nums:
			if n == 1:
				allones += 1
				onezero += 1
			else:
				onezero = allones
				allones = 0

			res = max(res, allones, onezero)

		return N - 1 if allones == N else res

"""
This leetcoder gives a sliding-window solution: 

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/708201/javaPython-3-Sliding-Window-with-at-most-one-zero-w-detailed-explanation-and-brief-analysis

The basic idea is to:

(a) Maintain a sliding window across nums that stretches from nums[i] to nums[j].
(b) Maintain a running count of the number of 1s within the sliding window

If sum == j - i + 1, then there are only 1s in the window stretching from nums[i] to nums[j].
If sum == j - i, then there is one 0 in that window.
If sum < j - i, then there are at least two 0s in the window.

It is OK for there to be one 0 in the window. But, whenever sum < j - 1, we want to shrink the window, by increasing i (and throwing out nums[i]).

Here is my Python implementation of the linked program:
"""

class Solution(object):
	def longestSubarray(self, nums):
		res = 0
		s = 0
		i = 0
		for j, n in enumerate(nums):
			s += n
			while i < j and s < j - i:
				s -= nums[i]
				i += 1
			res = max(res, j - i)
		return res

"""
This problem was a Daily Question for 8/23/2025. I solved it without reference to the previous solutions above. This program is based on the same fundamental idea as my original program, but this program is simpler and more space-efficient:
"""

class Solution(object):
	def longestSubarray(self, nums):
		prev = -1
		zeros = 0
		left = 0
		right = 0
		res = 0
		for n in nums:
			if n == 1:
				right += 1
			elif prev == 1:
				zeros = 1
				left = right
				right = 0
			else:
				zeros += 1

			if zeros == 1:
				res = max(res, left + right)
			else:
				res = max(res, right)	

			prev = n

		return res - 1 if res == len(nums) else res
