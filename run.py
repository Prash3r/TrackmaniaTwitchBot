#!/usr/bin/env python 
#-*- coding: utf-8 -*-

# im running this on Python 9.5.2

# if you use the .env file to configure your environment you should:
#  1.) install the python-dotenv 'pip install python-dotenv' (or use pipenv)
#  2.) uncomment the following two lines (untested)
# from dotenv import load_dotenv
# load_dotenv()

# vendor
import mariadb
import minidi

# local
from TTBot import TrackmaniaTwitchBot
from TTBot.logic.Environment import Environment
from TTBot.logic.MariaDbConnection import MariaDbConnection
from TTBot.logic.TwitchBotWrapper import TwitchBotWrapper

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

	pMariaDbConnection: MariaDbConnection = minidi.get(MariaDbConnection)
	pMariaDbConnection.set(pDb)
# def initDatabase()

if __name__ == '__main__':
	initDatabase()

	pTwitchBot = TrackmaniaTwitchBot()
	pTwitchBotWrapper: TwitchBotWrapper = minidi.get(TwitchBotWrapper)
	pTwitchBotWrapper.set(pTwitchBot)

	pTwitchBot.run()
# if __name__ == '__main__'