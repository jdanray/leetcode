# https://leetcode.com/problems/peeking-iterator/

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
	def __init__(self, iterator):
		self.iterator = iterator
		self.top = iterator.next()
		self.empty = False

	def peek(self):
		return self.top

	def next(self):
		ret = self.top
		if not self.iterator.hasNext():
			self.empty = True
		self.top = self.iterator.next()
		return ret

	def hasNext(self):
		return not self.empty
