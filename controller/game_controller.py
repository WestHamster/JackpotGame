# to keep track of user attempts, import PlayerService and PlayerController

from app.service.player_service import PlayerService
from app.controller.player_controller import PlayerController

playerController = PlayerController(PlayerService())

import random

class GameController(object):
	
	def __init__(self, gameService):
		self.gameService = gameService

	def addGame(self,id,slot,try_at,chance,playerId):
		"""
		For adding a new game
		"""
		return self.gameService.addGame(id, slot, try_at, chance, playerId)

	
	def getWinner(self, game_obj, player_obj):
		"""
		For finding the winner
		game_obj:  game, slot_number, try_at,chances, playerid
		player_obj: playerid, attempts
		"""
		print()
		print("Let's roll the dice")
		print()
		winner = False
		print("Player ID:", game_obj.playerId)
		for val in range(game_obj.chance):
			print("Chances left:", game_obj.chance)
			print()
			game_obj.chance -= 1

			# Add the attempt using PlayerController
			player_updation = playerController.increaseAttempt(player_obj, game_obj.try_at,game_obj.slot)
			
			slot_len = len(set(game_obj.slot))

			if slot_len<2:
				return True

			game_obj.try_at += 1
			game_obj.slot = self.gameService.generateRandomSlot(game_obj.slot)

		return False


	"""
	For making the attempts single time, add below code on line 28

	for val in range(game_obj.chance):
			game_obj.chance -= 1
			# player_obj[game_obj.try_at] = game_obj.slot
			player_updation = playerController.increaseAttempt(player_obj, game_obj.try_at,game_obj.slot)
			slot_len = len(set(game_obj.slot))
			if slot_len<2:
				return True

			print()
			check = input("Do you wish to continue? (Press any word to roll the dice or Enter to quit)")
			if not check:
				break
			
			game_obj.try_at += 1
			# print("Player updation:", player_updation.attempt)
			game_obj.slot = self.gameService.generateRandomSlot(game_obj.slot)
	"""