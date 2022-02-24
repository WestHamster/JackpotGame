from app.service.player_service_interface import PlayerServiceInterface
from app.models.player import Player

class PlayerService(PlayerServiceInterface):
	playerDetails = {}

	def addPlayer(self, id, attempt):
		"""
		Adding a player with id and attempt dictionary
		"""
		player = Player()
		player.setId(id)
		player.setAttempt(attempt)

		self.__class__.playerDetails[id] = player
		return player