#!/usr/bin/env python 
#-*- coding: utf-8 -*-

# im running this on Python 9.5.2

# if you use the .env file to configure your environment you should:
#  1.) install the python-dotenv 'pip install python-dotenv' (or use pipenv)
#  2.) uncomment the following two lines (untested)
# from dotenv import load_dotenv
# load_dotenv()

# pylib
import logging

# vendor
import mariadb
import minidi

# local
from TTBot import TrackmaniaTwitchBot
from TTBot.logic.DbConnection import DbConnection
from TTBot.logic.interface.DbQueryDialectConverter import DbQueryDialectConverter
from TTBot.logic.Environment import Environment
from TTBot.logic.Logger import Logger
from TTBot.logic.production.MariaDbQueryDialectConverter import MariaDbQueryDialectConverter
from TTBot.logic.interface.MessageConverter import MessageConverter
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper
from TTBot.logic.production.TwitchMessageConverter import TwitchMessageConverter

def initDatabase():
	pEnvironment: Environment = minidi.get(Environment)

	pDb = mariadb.connect(
		user     =     pEnvironment.getVariable('DBUSER') ,
		password =     pEnvironment.getVariable('DBPASS') ,
		host     =     pEnvironment.getVariable('DBHOST') ,
		port     = int(pEnvironment.getVariable('DBPORT')),
		database =     pEnvironment.getVariable('DBNAME')
	)
	pDb.autocommit = True
	pDb.auto_reconnect = True

	pDbConnection: DbConnection = minidi.get(DbConnection)
	pDbConnection.set(pDb)
# def initDatabase()
    
def initLogger():
	pEnvironment: Environment = minidi.get(Environment)
	pLogger: Logger = minidi.get(Logger)

	pLogger.setLevel(logging.DEBUG if pEnvironment.isDebug() else logging.INFO)
	pFormatter = logging.Formatter("%(asctime)s [%(levelname)s.%(funcName)s] %(message)s")
	pStreamHandler = logging.StreamHandler()
	pStreamHandler.setFormatter(pFormatter)
	pLogger.addHandler(pStreamHandler)
# def initLogger()

def initLogic():
	minidi.set(DbQueryDialectConverter, minidi.get(MariaDbQueryDialectConverter))
	minidi.set(MessageConverter, minidi.get(TwitchMessageConverter))
# def initLogic()

if __name__ == '__main__':
	initLogger()
	initDatabase()
	initLogic()

	pTwitchBot = TrackmaniaTwitchBot()

	pTwitchBotWrapper: TwitchBotWrapper = minidi.get(TwitchBotWrapper)
	pTwitchBotWrapper.set(pTwitchBot)

	pTwitchBot.run()
# if __name__ == '__main__'