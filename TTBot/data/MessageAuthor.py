class MessageAuthor:
	def __init__(self, **kwargs):
		self._isMod = kwargs.get('isMod', False)
		self._isSubscriber = kwargs.get('isSubscriber', False)
		self._name = kwargs.get('name', '')
	# def __init__(self, **kwargs)

	def getName(self) -> str:
		return self._name

	def isMod(self) -> bool:
		return self._isMod

	def isSubscriber(self) -> bool:
		return self._isSubscriber
# class MessageAuthor