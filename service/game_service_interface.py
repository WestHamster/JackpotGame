import abc

class GameServiceInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod

	def addGame(self,id,slot,try_at,chance,playerId):
		pass