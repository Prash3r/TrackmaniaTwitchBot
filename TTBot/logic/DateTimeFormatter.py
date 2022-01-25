# pylib
import datetime

# vendor
import minidi

class DateTimeFormatter(minidi.Injectable):
	def formatIntervalShort(self, pDelta: datetime.timedelta) -> str:
		days   = int(pDelta.days)

		hours  = int( pDelta.seconds / 60 / 60      )
		mins   = int((pDelta.seconds      / 60) % 60)
		secs   = int( pDelta.seconds            % 60)

		millis = int(pDelta.microseconds / 1000)
		micros = int(pDelta.microseconds % 1000)

		if pDelta < datetime.timedelta():
			# datetime.timedelta normalizes the data inside itself (-1us => -1d +86399s +999999us)
			# negative timedeltas are weird to handle, so we are not gonna bother
			raise ValueError('Can only format positive intervals!')

		if days > 0:
			return f'{days}d{hours}h' if hours > 0 else f'{days}d'
		elif hours > 0:
			return f'{hours}h{mins}m' if mins > 0 else f'{hours}h'
		elif mins > 0:
			return f'{mins}m{secs}s' if secs > 0 else f'{mins}m'
		elif secs > 0:
			return f'{secs}.{millis:03}s' if millis > 0 else f'{secs}s'
		elif millis > 0:
			return f'{millis}.{micros:03}ms' if micros > 0 else f'{millis}ms'
		else:
			return f'0.{micros:03}ms'
	# def formatIntervalShort(self, pDelta: datetime.timedelta) -> str
# class DateTimeFormatter(minidi.Injectable)