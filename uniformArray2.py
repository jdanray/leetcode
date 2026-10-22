# https://leetcode.com/problems/construct-uniform-parity-array-ii/ 

"""
If all the elements have the same parity, return true.

To change an element's parity, we must subtract a number from it that is odd and smaller than it. So, we find the smallest odd number; if that's not smaller than a given element, then no odd number is. So, we let m be the smallest odd we've seen so far, and every time we see an odd, we update m. So, if m is still float('inf') in the end, then nums1 is all evens, and we return true. We also count the odds we see, and if nums1 is all odds, we return true. Finally, we check whether m can be subtracted from each even. 

Note: You cannot construct an all-evens array. To do so, you would have to subtract from the smallest odd number an odd number that is smaller than it.
"""

class Solution(object):
	def uniformArray(self, nums1):
		o = 0
		m = float('inf')
		for n in nums1:
			if n % 2 == 1:
				o += 1
				m = min(m, n)

		return o == len(nums1) or m == float('inf') or not any(n % 2 == 0 and n - m < 1 for n in nums1)

"""
Optimization: You don't need to test every even. You just need to find the smallest even: You can convert the array IFF you can subtract m from the smallest even. For if you cannot subtract m from it, then you cannot convert every element. And if you can subtract m from it, then you can also subtract m from every other even number, and the whole array is convertible.
"""

class Solution(object):
	def uniformArray(self, nums1):
		no = 0
		mo = float('inf')
		me = float('inf')
		for n in nums1:
			if n % 2 == 1:
				no += 1
				mo = min(mo, n)
			else:
				me = min(me, n)

		return no == len(nums1) or mo == float('inf') or me - mo >= 1
