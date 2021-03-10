# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

"""
Let s1 be sum(nums1), s2 be sum(nums2).

Some possibilities:

s1 == s2
	Return 0
s1 > s2
	Decrease s1 and/or increase s2
s1 < s2
	Increase s1 and/or decrease s2
	Idea. Swap s1,s2 and run s1>s2 procedure on this case

The problem is that s1 != s2. We want to change nums1 and/or nums2, so that s1 == s2. There are many sequences of changes you could make that will result in s1 == s2. Return the fewest number of changes required. 

If s1 == s2, there is no problem. We can just report that we made 0 changes. 

While s1 > s2 and changes can be made, make the biggest possible changes. Start with nums1. Change nums2 if needed.

A change in nums1 can cause either an increase or decrease in s1.
A change in nums2 can cause either an increase or decrease in s2.

If s1 > s2, first try to decrease s1. If that doesn't succeed, then try to increase s2. Greedily make the largest decreases and increases possible.

Stick nums1 in a max priority queue. Pop the largest number. Take it all the way down to 1. If doing that closes the gap between s1 and s2, then we're done.
Stick nums2 in a min priority queue. Pop the smallest number. Increase it up to 6. If doing that closes the gap between s1 and s2, then we're done.

You DON'T need a priority queue. Just sort nums1 and nums2.
We can also pop from nums1 and nums2 in the same iteration, so that you don't need to go through nums1 and then through nums2.

...

Although the design of the finished product has some similarities to the original design, the program ended up going in a different direction.

I realized that it's bad to start with nums1. Even if you then consider nums2 in the same iteration, that plan doesn't work, because it may be better to modify nums2 (decrease s2) first.

The key idea is to consider the differences between 1 and 6, for nums1 and nums2 (respectively). Generate those differences, and store them in a list. If the sum of them is g.t.e. the difference between s1 and s2, then you can modify nums1 and nums2, so that s1 == s2. To find the minimum number of operations, sort the list and greedily sum up the increases/decreases in order of size. In this way, you can execute the greedy algorithm properly. If, in contrast, you consider nums1 and then nums2, you might not consider the largest possible changes in their proper order. 
"""

class Solution(object):
	def minOperations(self, nums1, nums2):
		lo = 1
		hi = 6

		s1 = sum(nums1)
		s2 = sum(nums2)
		if s1 < s2:
			s1, s2 = s2, s1
			nums1, nums2 = nums2, nums1

		nums3 = [n1 - lo for n1 in nums1] + [hi - n2 for n2 in nums2]
		nums3 = sorted(nums3)

		d = s1 - s2
		res = 0
		while d > 0 and nums3:
			d -= nums3.pop()
			res += 1

		return res if d <= 0 else -1

"""
After I solve problems, I like to study other people's solutions. The following comment made me appreciate that O(N*lg(N)) sorting isn't necessary:

https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/discuss/1085786/JavaPython-3-2-Greedy-codes%3A-sort-and-count-w-brief-explanation-and-analysis.

Instead, we can use a counter, fixed for 0 to 5. That will reduce the complexity of the program to O(N) time and O(1) space. Here is my Python implementation of the idea:
"""

class Solution(object):
	def minOperations(self, nums1, nums2):
		lo = 1
		hi = 6

		s1 = sum(nums1)
		s2 = sum(nums2)
		if s1 < s2:
			s1, s2 = s2, s1
			nums1, nums2 = nums2, nums1

		count = [0 for _ in range(hi)]
		for n1 in nums1:
			count[n1 - lo] += 1
		for n2 in nums2:
			count[hi - n2] += 1 

		d = s1 - s2
		i = hi - 1
		res = 0
		while d > 0 and i > 0:
			while d > 0 and count[i] > 0:
				d -= i
				count[i] -= 1
				res += 1
			i -= 1

		return res if d <= 0 else -1
