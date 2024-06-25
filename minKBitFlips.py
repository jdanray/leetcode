# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/ 

"""
This problem was pretty easy. It is very similar to two problems that I solved in yesterday's contest:

https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

The fundamental idea is the same in all solutions: Do a flip only if necessary. The minimum number of flips is the strictly necessary number of flips. So, do a flip iff the current value of nums[i] is 0.

A crucial thing to observe is that, because of the flips, the current value of nums[i] might not be the same as nums[i]. For each nums[i], you have to answer the question: What is the current value of nums[i]? 

If you know the number of times that nums[i] has been flipped, you can determine its current value. So, every time you do a flip, store the index in the deque F. A loop invariant will be that F consists of the indexes for flips that affected nums[i], in sorted order. To maintain the invariant, while i - F[0] >= k, we pop F[0]. Now len(F) is the number of times that nums[i] has been flipped.

If len(F) is even, then the current value of nums[i] is nums[i]. If len(F) is odd, then the current value is the reverse of nums[i]. So, if len(F) % 2 == nums[i], we try to do a flip. If there aren't k or more elements remaining in nums, we return -1.
"""

class Solution(object):
	def minKBitFlips(self, nums, k):
		flips = collections.deque()
		res = 0
		for i, n in enumerate(nums):
			while flips and i - flips[0] >= k:
				flips.popleft()

			if len(flips) % 2 == n:
				if len(nums) - i < k:
					return -1
				else:
					flips.append(i)
					res += 1

		return res

"""
After I solve a problem, I like to study other people's solutions. I found a more space-efficient solution here:

https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/238609/JavaC%2B%2BPython-One-Pass-and-O(1)-Space

It turns out that you don't need to store any indexes. If you modify nums[i] to indicate when it's been flipped, you can just keep track of the number of flips. 

Here is my implementation of the idea:
"""

class Solution(object):
	def minKBitFlips(self, nums, k):
		flips = 0
		res = 0
		for i, n in enumerate(nums):
			if i >= k and nums[i - k] > 1:
				nums[i] -= 2
				flips -= 1

			if flips % 2 == n:
				if len(nums) - i < k:
					return -1
				else:
					nums[i] += 2
					flips += 1
					res += 1

		return res
