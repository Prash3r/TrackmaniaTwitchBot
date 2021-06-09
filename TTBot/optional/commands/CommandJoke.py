# pylib
#import time
import random
# local
from .Command import Command

class CommandJoke(Command):
    
    @staticmethod
    def getCommandString() -> str:
        return 'joke'
    
    @staticmethod
    def getRightsId() -> str:
        return 'joke'

    async def execute(self, args) -> str:
        if self.messageAuthor.lower() == "fegir":
            return 'kem1W'
        if self.messageAuthor.lower() == "amaterasutm":
            if random.choice([True, False, False, False, False, False, False]):
                return 'kem1W'
            else:
                return 'you know who!'
        else:
            if random.choice([True, False, False, False, False, False, False]):
                return self.messageAuthor   # ToDo the message author should be stored in correct capitalization instead of lowercase for this to work properly
                #time.sleep(1)      # could be possible if planned msgs is a thing
                #return 'Fegir'
                #time.sleep(2)      # alternatively create another return class -> multiAnswer ..
                #return 'KEKW'
            else:
                return 'Fegir'