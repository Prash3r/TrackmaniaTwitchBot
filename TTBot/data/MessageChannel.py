class MessageChannel:
	def __init__(self, **kwargs):
		self._name        = kwargs.get('name'       , '')
		self._sendMessage = kwargs.get('sendMessage', None)
	# def __init__(self, **kwargs)

	def getName(self) -> str:
		return self._name
	
	async def sendMessage(self, message: str):
		if self._sendMessage:
			await self._sendMessage(message)
# class MessageChannel