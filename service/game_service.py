from app.service.game_service_interface import GameServiceInterface
from app.models.game import Game
import random

class GameService(GameServiceInterface):
	gameDetails = {}

	def addGame(self, id, slot, try_at, chance, playerId):
		"""
		Adding game model and using setter to set the value
		"""
		game = Game()
		game.setId(id)
		game.setSlot(slot)
		game.setTry(try_at)
		game.setChance(chance)
		game.setPlayerId(playerId)

		self.__class__.gameDetails[id] = game
		return game

	def generateRandomSlot(self, slot_values):
		"""
		Generating random list of number for 3 slots
		"""
		return [random.randint(0,9), random.randint(0,9), random.randint(0,9)]
