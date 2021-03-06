# pylib
import datetime

# local
from TTBot.data.Message import Message
from TTBot.logic.DateTimeFormatter import DateTimeFormatter
from TTBot.module.Command import Command
from TTBot.module.cotd.CotdInfo import CotdInfo
from TTBot.module.cotd.CotdInfoCache import CotdInfoCache
from TTBot.module.cotd.CotdInfoFactory import CotdInfoFactory
from TTBot.module.cotd.TrackmaniaIoCotd import TrackmaniaIoCotd

class CommandCotd(Command):
    pCotdInfoCache: CotdInfoCache
    pCotdInfoFactory: CotdInfoFactory
    pDateTimeFormatter: DateTimeFormatter
    pTrackmaniaIoCotd: TrackmaniaIoCotd
    
    def getCommandTrigger(self):
        return 'cotd'
    
    def getModuleId(self) -> str:
        return 'cotd'

    def _buildCotdInfoMessage(self) -> str:
        self.pTrackmaniaIoCotd.loadInfo()

        pCotdInfoPrev = self.pCotdInfoCache.getPrev()
        pCotdInfoNext = self.pCotdInfoCache.getNext()
        if not pCotdInfoNext:
            pCotdInfoNext = self.pCotdInfoFactory.createNext(pCotdInfoPrev)

        pNow = datetime.datetime.now()
        pDelta = pNow - pCotdInfoPrev.getDateEnd()
        infoPrev = f'Last CotD finished {self.pDateTimeFormatter.formatIntervalShort(pDelta)} ago, winner: {pCotdInfoPrev.getWinner()}'
        
        pDelta = pCotdInfoNext.getDateStart() - pNow
        infoNext = f'next CotD starts in ~{self.pDateTimeFormatter.formatIntervalShort(pDelta)}'

        return f'{infoPrev} // {infoNext}'
    # def _buildCotdInfoMessage(self) -> str

    def _buildCotdPlayerInfoMessage(self, playerName: str) -> str:
        return 'coming soon ... PauseChamp'
    # def _buildCotdPlayerInfoMessage(self, playerName: str) -> str

    async def execute(self, pMessage: Message, args: list[str]) -> str:
        messageAuthorName = pMessage.getAuthor().getName()
        
        if not args:
            return f'@{messageAuthorName} {self._buildCotdInfoMessage()}'
        
        playerName = args[0]
        return f'@{messageAuthorName} {self._buildCotdPlayerInfoMessage(playerName)}'
    # async def execute(self, pMessage: Message, args: list[str]) -> str
# class CommandCotd(Command)