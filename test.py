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
import os
import sqlite3

# vendor
import minidi

# local
from TTBot.logic.DbConnection import DbConnection
from TTBot.logic.interface.DbQueryDialectConverter import DbQueryDialectConverter
from TTBot.logic.Logger import Logger
from TTBot.logic.development.SqliteQueryDialectConverter import SqliteQueryDialectConverter
from TTBot.logic.development.TerminalMessageConverter import TerminalMessageConverter
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper
from TTBot.optional.commands.CommandRunner import CommandRunner
from TTBot.optional.evaluators.EvaluatorRunner import EvaluatorRunner

def initDatabase():
	minidi.set(DbQueryDialectConverter, minidi.get(SqliteQueryDialectConverter))

	pSqliteDbConnection = sqlite3.connect('test.sqlite', isolation_level=None)
	pDbConnection: DbConnection = minidi.get(DbConnection)
	pDbConnection.set(pSqliteDbConnection)

	pDbConnection.query("PRAGMA encoding = 'UTF-8';")
# def initDatabase()

def initEnvironment():
	os.environ['TWITCH_BOT_USERNAME'] = 'terminal'
	os.environ['TWITCH_CMD_PREFIX'] = '!'
# def initEnvironment()
    
def initLogger():
	pLogger: Logger = minidi.get(Logger)

	pLogger.setLevel(logging.DEBUG)
	pFormatter = logging.Formatter("%(asctime)s [%(levelname)s.%(funcName)s] %(message)s")
	pStreamHandler = logging.StreamHandler()
	pStreamHandler.setFormatter(pFormatter)
	pLogger.addHandler(pStreamHandler)
# def initLogger()

class TwitchBotMock:
	async def join_channels(self, _: list):
		pass
# class TwitchBotMock

def initTwitchBotMock():
	pTwitchBotMock = TwitchBotMock()
	pTwitchBotWrapper: TwitchBotWrapper = minidi.get(TwitchBotWrapper)
	pTwitchBotWrapper.set(pTwitchBotMock)
# def initTwitchBotMock()

if __name__ == '__main__':
	initEnvironment()
	initLogger()
	initDatabase()
	initTwitchBotMock()

	pCommandRunner: CommandRunner = minidi.get(CommandRunner)
	pEvaluatorRunner: EvaluatorRunner = minidi.get(EvaluatorRunner)
	pMessageConverter: TerminalMessageConverter = minidi.get(TerminalMessageConverter)

	while True:
		chatMessage = input('> ')
		pMessage = pMessageConverter.convert(chatMessage)

		try:
			loop = asyncio.get_event_loop()
			pCommandCoroutine = pCommandRunner.execute(pMessage)
			pEvaluatorCoroutine = pEvaluatorRunner.execute(pMessage)

			loop.run_until_complete(pCommandCoroutine)
			loop.run_until_complete(pEvaluatorCoroutine)
		except Exception as e:
			print(e.__class__.__name__, '->', e)
	# while True
# if __name__ == '__main__'