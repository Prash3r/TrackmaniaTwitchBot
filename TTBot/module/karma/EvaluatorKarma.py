# pylib
import re

# local
from TTBot.data.Message import Message
from TTBot.logic.LocalVariables import LocalVariables
from TTBot.module.Evaluator import Evaluator

class EvaluatorKarma(Evaluator):
	pLocalVariables: LocalVariables

	def getMessageRegex(self) -> str:
		return r'(--|\+\+)'
	
	def getModuleId(self) -> str:
		return 'karma'

	def _buildVoteMessage(self, plusVotes: int, minusVotes: int) -> str:
		if plusVotes >= 1 and minusVotes >= 1:
			return f'++ (x{plusVotes}), -- (x{minusVotes})'
		elif plusVotes >= 1 and minusVotes == 0:
			return f'++ (x{plusVotes})' if plusVotes >= 2 else '++'
		elif plusVotes == 0 and minusVotes >= 1:
			return f'-- (x{minusVotes})' if minusVotes >= 2 else '--'
		else:
			return 'kem1W'
	# def _buildVoteMessage(self, plusVotes: int, minusVotes: int) -> str

	def _countMinusVotes(self, message: str) -> int:
		# string starts with --, or before a -- is not a -
		return self._countVotes(r'^-[-]+|[^-]-[-]+', message)
	# def _countMinusVotes(self, message: str) -> int

	def _countPlusVotes(self, message: str) -> int:
		# string starts with ++, or before a ++ is not a +
		return self._countVotes(r'^\+[\+]+|[^\+]\+[\+]+', message)
	# def _countPlusVotes(self, message: str) -> int

	def _countVotes(self, regex: str, message: str) -> int:
		return len(re.findall(regex, message))
	
	async def execute(self, pMessage: Message) -> str:
		pChannel = pMessage.getChannel()
		channelName = pChannel.getName()

		message = pMessage.getContent()
		plusVotes = min(1, self._countPlusVotes(message))
		minusVotes = min(1, self._countMinusVotes(message))

		currentKarma = self.pLocalVariables.get('karma', channelName, 0)
		newKarma = currentKarma + plusVotes - minusVotes
		self.pLocalVariables.write('karma', channelName, newKarma)

		voteMessage = self._buildVoteMessage(plusVotes, minusVotes)

		return f"Successfully voted {voteMessage}, current streamer karma: {newKarma}"
	# async def execute(self, pMessage: Message) -> str
# class EvaluatorKarma(Evaluator)