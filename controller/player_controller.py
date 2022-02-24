# Allocating different controller function to operate on player object
class PlayerController(object):
	def __init__(self,playerService):
		self.playerService = playerService

	def addPlayer(self, id, attempt):
		return self.playerService.addPlayer(id,attempt)

	def increaseAttempt(self,player,key,attempt):
		player.attempt[key] = attempt
		return player