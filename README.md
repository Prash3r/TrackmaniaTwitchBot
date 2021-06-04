# TTBot - Trackmania Twitch Bot

This is the repository of the [twitch.tv bot trackmania_bot](https://www.twitch.tv/trackmania_bot). Its main capability right now is that it can look up matchmaking rankings via [trackmania.io](https://trackmania.io/#/players). Additionaly there are some commands and evaluators implemented that are channel specific.

You came here for one of 2 reasons:
 - [i want this bot in my channel](##%20I%20want%20this%20bot%20in%20my%20channel)
 - [i need help configuring the bot](##%20I%20need%20help%20configuring%20the%20bot)
 - [i want to implement additional functionality](##%20I%20want%20to%20implement%20additional%20functionality)

You came to the right place. The current version is hosted and will be pulled regurarily from this repository. There is no need to host a copy or register your own bot - although you are free to do that. 

## I want this bot in my channel
go to the bots chat [twitch.tv bot trackmania_bot](https://www.twitch.tv/trackmania_bot) and type `!invite`

the bot will now join your channel (obviously only possible for the streamer himself). If you want the bot to leave type !uninvite either in the bots channel or in your own. Be mindful, this deletes all of your configuration.
## I need help configuring the bot
the basic commands `!uninvite`, `!help` and `!module` should always work and are only available for the streamer.

If you want to add an existing module you can add it via:

    !module add modulename

the functionality of modulname would be available for everyone in your channel. If you only want it to be invokeable by a subset of your users you can add an accesslevel integer as 3rd argument:

    !module add modulename 5
acesslevel 5 would mean the commands is only invokeable by subscribers.

currently implemented access levels:

 - **100** owner of the channel
 - **10** moderators
 - **5** subscribers
 - **1** everyone

# Modules: commands and evaluators
All modules are either a command or an evaluator and they are located here:

 - [/TTBot/optional/commands](https://github.com/prash3r/TTBot/tree/master/TTBot/optional/commands) if they are commands (message starting with !)
 - [/TTBot/optional/evaluators](https://github.com/prash3r/TTBot/tree/master/TTBot/optional/commands) if they are evaluators (all messages need to be analyzed)

## I want to implement additional functionality
Feel free to create pull requests. This is an early stage of development so if you want to implement general functionality you maybe should talk to me first - chances are that someone is already doing it. If you want to implement a command or an evaluator you should look at an existing one first.

If you got your logic down you need to import it into the class like all the other optionals at [\_\_init\_\_.py](https://github.com/prash3r/TTBot/tree/master/TTBot/__init__.py). Evaluators have to be called individually from [_handle.py](https://github.com/prash3r/TTBot/tree/master/TTBot/_handle.py). Add them exactly as all other evaluators to the bottom of the list. Evaluators should also return if they triggered as bool.

You also need a new column in the [\_db.py](https://github.com/prash3r/TTBot/tree/master/TTBot/_db.py) creationcmds modules table that should be exactly named as your module. (this table is only created when empty so i have to add the column manually anyway. But it should work for a fresh start)

**If you have no means of testing just commit your newmodulename.py into evaluators or commands and i will test and integrate them.**

### Some Tips and examples

 - if you need a **persistent variable** look at the evaluator [luckerscounter](https://github.com/prash3r/TTBot/tree/master/TTBot/optional/evaluators/luckerscounter.py) and add your variable to the PV in [_db.py](https://github.com/prash3r/TTBot/tree/master/TTBot/_db.py) accordingly
 - some useful functions can be found in [_tools.py](https://github.com/prash3r/TTBot/tree/master/TTBot/_tools.py)

### Guidelines

 1. dont commit sensitive data
 2. dont commit your local SQLite database
 3. dont commit format changes if you didnt change the code
 4. preferrably rebase before pull request
 5. you should usually only commit 2 to 4 files for a pull request that only adds a command/evaluator
	 - **\_\_init\_\_.py**
	 - **newmodulename.py**
	 - **\_db.py** for the new module column in the Database (+ processvar if needed)
	 - _handle.py if its an evaluator
 6. please for the love of software dont commit your .env file

### Roadmap

 1. local testing
 2. alternative SQLite interface also for local testing
