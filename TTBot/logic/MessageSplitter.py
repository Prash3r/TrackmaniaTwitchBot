# vendor
import minidi

class MessageSplitter(minidi.Injectable):
	def split(self, string: str, splitters: list[str], maxLength: int) -> list[str]:
		splits = []

		while string:
			if len(string) <= maxLength:
				splits.append(string)
				return splits
			# if len(stringSlice) < maxLength

			# find the latest possible split index, prioritize earlier splitters
			stringSlice, string = string[:maxLength], string[maxLength:]
			splitIndices = self._rindices(stringSlice, splitters)
			splitIndex = -1
			
			for i in splitIndices:
				if i >= 0:
					splitIndex = i
					break
			# for i in splitIndices

			if splitIndex == -1:
				# no appropriate split found, hard cut the rest
				splits.append(stringSlice)
				while string:
					stringSlice, string = string[:maxLength], string[maxLength:]
					splits.append(stringSlice)
				return splits
			# if splitIndex == -1

			# split via splitter
			splitter = splitters[splitIndices.index(splitIndex)]

			splits.append(stringSlice[:splitIndex])
			string = stringSlice[splitIndex+len(splitter):] + string[:maxLength]
		# while True
	# def split(self, string: str, splitters: list[str], maxLength: int) -> list[str]

	def _rindices(self, string: str, subs: str) -> list[int]:
		return [self._rindex(string, sub) for sub in subs]
	# def _rindices(self, string: str, subs: str) -> list[int]

	def _rindex(self, string: str, sub: str) -> int:
		try:
			return string.rindex(sub)
		except ValueError:
			return -1
	# def _rindex(self, string: str, sub: str) -> int
# class MessageSplitter(minidi.Injectable)