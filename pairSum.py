# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/ 

class Solution(object):
	def pairSum(self, head):
		nums = []
		while head:
			nums.append(head.val)
			head = head.next

		i = 0
		j = len(nums) - 1
		res = 0
		while i < j:
			res = max(res, nums[i] + nums[j])
			i += 1
			j -= 1

		return res

"""
After I solve problems, I like to study other people's solutions. I found the following solution that uses O(1) space:

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/discuss/1675762/Variation-of-Palindrome-check-of-Linked-List-in-Constant-Space

I translated the C++ code into Python:
"""

class Solution(object):
	def pairSum(self, head):
		# find midpoint
		prev = None
		slow = head
		fast = head
		while fast and fast.next:
			prev = slow
			slow = slow.next
			fast = fast.next.next

		# separate list into two halves
		prev.next = None

		# reverse second half
		prev = None
		while slow:
			slow.next, prev, slow = prev, slow, slow.next

		# search both halves
		head1 = head
		head2 = prev
		res = 0
		while head1 and head2:
			res = max(res, head1.val + head2.val)
			head1 = head1.next
			head2 = head2.next

		return res
