#!/usr/bin/env python 
#-*- coding: utf-8 -*-

# Launches the local test mode to test the bot under

# if you use the .env file to configure your environment you should:
#  1.) install the python-dotenv 'pip install python-dotenv' (or use pipenv)
#  2.) uncomment the following two lines (untested)
# from dotenv import load_dotenv
# load_dotenv()

# pylib
import asyncio
import logging
from unittest import mock
import os
import sqlite3

# vendor
import minidi

# local
from TTBot.logic.development.SqliteQueryDialectConverter import SqliteQueryDialectConverter
from TTBot.logic.development.TerminalMessageConverter import TerminalMessageConverter
from TTBot.logic.interface.DbQueryDialectConverter import DbQueryDialectConverter
from TTBot.logic.interface.MessageConverter import MessageConverter
from TTBot.logic.DbConnection import DbConnection
from TTBot.logic.Logger import Logger
from TTBot.logic.MessageEvaluator import MessageEvaluator
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper
from TTBot.module.ModuleRunner import ModuleRunner


class TwitchBotMock:
	async def join_channels(self, _: list):
		pass
# class TwitchBotMock


def initDatabase():
	pSqliteDbConnection = sqlite3.connect('test.sqlite', isolation_level=None)
	pDbConnection: DbConnection = minidi.get(DbConnection)
	pDbConnection.set(pSqliteDbConnection)

	pDbConnection.query("PRAGMA encoding = 'UTF-8';")
# def initDatabase()
    
def initLogger():
	pLogger: Logger = minidi.get(Logger)

	pLogger.setLevel(logging.DEBUG)
	pFormatter = logging.Formatter("%(asctime)s [%(levelname)s.%(funcName)s] %(message)s")
	pStreamHandler = logging.StreamHandler()
	pStreamHandler.setFormatter(pFormatter)
	pLogger.addHandler(pStreamHandler)
# def initLogger()

def initRuntimeEnvironment():
	os.environ['TWITCH_BOT_USERNAME'] = 'terminal'
	os.environ['TWITCH_CMD_PREFIX'] = '!'

	minidi.set(DbQueryDialectConverter, minidi.get(SqliteQueryDialectConverter))
	minidi.set(MessageConverter, minidi.get(TerminalMessageConverter))

	pMessageEvaluator: MessageEvaluator = minidi.get(MessageEvaluator)
	pMessageEvaluator.isMainDeveloperMessage = mock.Mock(return_value=True)

	pTwitchBotMock = TwitchBotMock()
	pTwitchBotWrapper: TwitchBotWrapper = minidi.get(TwitchBotWrapper)
	pTwitchBotWrapper.set(pTwitchBotMock)
# def initRuntimeEnvironment()

if __name__ == '__main__':
	initRuntimeEnvironment()
	initLogger()
	initDatabase()

	pModuleRunner: ModuleRunner = minidi.get(ModuleRunner)
	pMessageConverter: MessageConverter = minidi.get(MessageConverter)

	while True:
		chatMessage = input('> ')
		pMessage = pMessageConverter.convert(chatMessage)

		try:
			loop = asyncio.get_event_loop()
			pModuleCoroutine = pModuleRunner.execute(pMessage)
			loop.run_until_complete(pModuleCoroutine)
		except Exception as e:
			print(e.__class__.__name__, '->', e)
	# while True
# if __name__ == '__main__'