# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/ 

"""
Your task is to use swaps to create an alternating string out of a given string

Now, any alternating string begins with either '1' or '0'. This provides the idea for a plan:

[1] Determine whether you can create a '1'-alternating string. If you can, count the number of swaps it takes
[2] Determine whether you can create a '0'-alternating string. If you can, count the number of swaps it takes
[3] Return the minimum number of swaps between the two. Since there are only these two possible kinds of alternating strings, this must be the absolute minimum

You can create an alternating string IFF there are equal numbers of 1's and 0's out-of-place

Whether a bit is out-of-place depends on whether the string is '1'-alternating or '0'-alternating

If an alternating string begins with '1', then '10' repeats throughout the string. Eg: '10101010'. So, a '0' is out-of-place if it occupies an even-numbered index, and a '1' is out-of-place if it occupies an odd-numbered index. Parallel reasoning applies to '0'-alternating strings
"""

class Solution(object):
	def minSwaps(self, s):
		zeros1 = 0
		ones1 = 0
		zeros2 = 0
		ones2 = 0
		for i, b in enumerate(s):
			# count the out-of-place 1's and 0's

			"""
			# check 1st pattern: '10' pattern
			if i % 2 == 0 and b != '1':
				ones1 += 1
			elif i % 2 == 1 and b != '0':
				zeros1 += 1

			# now check '01' pattern
			if i % 2 == 0 and b != '0':
				zeros2 += 1
			elif i % 2 == 1 and b != '1':
				ones2 += 1
			"""

			if b == '1':
				if i % 2 == 0:
					zeros2 += 1
				else:
					zeros1 += 1
			elif i % 2 == 0:
				ones1 += 1
			else:
				ones2 += 1

		if zeros1 == ones1 and zeros2 == ones2:
			return min(zeros1, zeros2)
		elif zeros1 == ones1:
			return zeros1
		elif zeros2 == ones2:
			return zeros2
		else:
			return -1
