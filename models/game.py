# Initialising Game model

class Game(object):
	def __init__(self):
		self.id = None
		self.slot = None
		self.try_at = None
		self.chance = None
		self.playerId = None

	def setId(self,id):
		self.id = id

	def getId(self,id):
		return self.id

	def setSlot(self,slot):
		self.slot = slot

	def getSlot(self,slot):
		return self.slot

	def setTry(self,try_at):
		self.try_at = try_at

	def getTry(self,try_at):
		return self.try_at

	def setChance(self,chance):
		self.chance = chance

	def getChance(self,chance):
		return self.chance

	def setPlayerId(self,playerId):
		self.playerId = playerId

	def getPlayerId(self,playerId):
		return self.playerId
	