# https://leetcode.com/problems/my-calendar-i/ 

class MyCalendar(object):
	def __init__(self):
		self.events = []

	def book(self, start, end):
		for (s, e) in self.events:
			if (start <= s < end) or (start < e <= end) or (s <= start and end <= e):
				return False

		self.events.append((start, end))
		return True
