import sys
import random

# append the path to your project to avoid warnings and directory errors
sys.path.append('/Users/ankuranand/Desktop/LLD')


from app.controller.player_controller import PlayerController
from app.controller.game_controller import GameController


# programmed to interface not to implementation
from app.service.player_service import PlayerService
from app.service.game_service import GameService

playerController = PlayerController(PlayerService())
gameController = GameController(GameService())



attempts = {}
# configured for 3 slots
slots_number = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]


#################################
#		SAMPLE TEST CASE		#
#################################

# adding players and games
# Player object contains -> id, attempt (dictionary containing the attempts)
player1 = playerController.addPlayer("player1",{})
print()
# Game object contains -> id, slots, try_at, chance, playerId
gameController1 = gameController.addGame("game1",slots_number,1,10,"player1")
print("Game chances left:",gameController1.chance)
winner = gameController.getWinner(gameController1, player1)


################################# 
# To print the attempts

print(player1.id," attempts:",player1.attempt)


# To get the exact attempt number
# player1.attempt.get(1)
#################################




if winner:
	print()
	print()
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("ER\tWINNER\t\tWINNER\t\tWINN")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
else:
	print()
	print()
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("E!\tBETTER LUCK NEXT TIME!\t\tBETT")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")