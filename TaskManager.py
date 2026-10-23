# https://leetcode.com/problems/design-task-manager/

class TaskManager(object):
	def __init__(self, tasks):
		self.tasks = []
		heapq.heapify(self.tasks)

		self.priority = dict()
		self.user = dict()

		for (u, t, p) in tasks:
			self.add(u, t, p)

	def add(self, userId, taskId, priority):
		self.priority[taskId] = priority
		self.user[taskId] = userId
		heapq.heappush(self.tasks, (-priority, -taskId))

	def edit(self, taskId, newPriority):
		self.add(self.user[taskId], taskId, newPriority)

	def rmv(self, taskId):
		self.priority[taskId] = None

	def execTop(self):
		if not self.tasks:
			return -1

		p, t = heapq.heappop(self.tasks)
		while self.tasks and (self.priority[-t] == None or p != -self.priority[-t]):
			p, t = heapq.heappop(self.tasks)

		if self.priority[-t] == None:
			return -1
		else:
			self.rmv(-t)
			return self.user[-t]