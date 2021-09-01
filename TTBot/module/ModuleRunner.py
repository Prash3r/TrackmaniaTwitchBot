# vendor
import minidi

# local
from TTBot.data.Message import Message
from TTBot.module.CommandRunner import CommandRunner
from TTBot.module.EvaluatorRunner import EvaluatorRunner

class ModuleRunner(minidi.Injectable):
	pCommandRunner: CommandRunner
	pEvaluatorRunner: EvaluatorRunner

	async def execute(self, pMessage: Message):
		await self.pCommandRunner.execute(pMessage)
		await self.pEvaluatorRunner.execute(pMessage)
	# async def execute(self, pMessage: Message)
# class ModuleRunner(minidi.Injectable)