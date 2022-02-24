# Initialising Player model
class Player(object):
	def __init__(self):
		self.id = None
		self.attempt = {}

	def setId(self,id):
		self.id = id

	def getId(self,id):
		return self.id

	def setAttempt(self,attempt):
		self.attempt = attempt

	def getAttempt(self,attempt):
		return self.attempt
