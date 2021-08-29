class MessageChannel:
	def __init__(self, **kwargs):
		self._name = kwargs.get('name', '')
	# def __init__(self, **kwargs)

	def getName(self) -> str:
		return self._name
# class MessageChannel