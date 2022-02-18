##############################################################################################
##############################################################################################
#POT GAME							JACKPOT GAME							JACKPOT GAME	 #
##############################################################################################
##############################################################################################



##############################################################################################
#									Installation											 #
##############################################################################################

1. Python3



##############################################################################################
#									HOW TO RUN?												 #
##############################################################################################

1. Add the path where you download this app in main.py file.
2. To run the sample test case, enter the following command in terminal -> python3 main.py
3. To add test-cases, please follow the sample test case method.
4. For adding more slots, please refer to folder wise documentation stated below.




##############################################################################################
#									DOCUMENTATION											 #
##############################################################################################


#################
#    MODELS		#
#################

1. Game:
	1.1 id : Game id
	1.2 slot : Slot values (in a form of list)
	1.3 try_at : Try attempts
	1.4 chance : Number of chances
	1.5 playerId : Player id

2. Player:
	2.1 id : Player id
	2.2 attempt: Player's attempt in a form of dictionary

All class contains constructors
All calls done are in the form of setters and getters


#################
#    Service	#
#################

1. Game
	1.1 Game Service Interface:
		1.1.1 addGame : for adding game (abstract class)
	1.2 Game Service:
		1.2.1 addGame : for setting the values of games using setter
		1.2.2 generateRandomSlot : for generating Random numbers in the list 
									of 3 numbers


2. Player
	2.1 Player Service Interface:
		2.1.1 addPlayer : for adding player (abstract class)
	2.2 Player Service:
		2.2.1 addPlayer : for setting the values of games using setter


#################
#   Controller	#
#################

1. Game
	1.1 addGame : To add a new game
		returns: gameService adding game

	1.2 getWinner : To roll different chances to find a winner
		returns: True / False

		Miscellaneous : another logic added below for single time execution

2. Player
	2.1 addPlayer : To add a new player
		returns: PlayerService adding player

	2.2 increaseAttempt : To update the player attempt in dictionary
		returns: player object

All class contains constructors where Services are called as the Programming is 
done to interface and not to implementation