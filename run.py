#!/usr/bin/env python 
#-*- coding: utf-8 -*-

# im running this on Python 9.5.2

# if you use the .env file to configure your environment you should:
#  1.) install the python-dotenv 'pip install python-dotenv' (or use pipenv)
#  2.) uncomment the following two lines (untested)
# from dotenv import load_dotenv
# load_dotenv()

import TTBot
TTBot = TTBot.TrackmaniaTwitchBot()
TTBot.run()