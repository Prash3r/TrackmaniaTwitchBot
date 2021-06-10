# TTBot - Trackmania Twitch Bot

This is the repository of the [twitch.tv bot trackmania_bot](https://www.twitch.tv/trackmania_bot). Its main capability right now is that it can look up matchmaking rankings via [trackmania.io](https://trackmania.io/#/players). Additionaly there are some commands and evaluators implemented that are channel specific.

You came here for one of 2 reasons:
 - i want this bot in my channel
 - i need help configuring the bot
 - i want to implement additional functionality

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

 - [/TTBot/optional/commands](https://github.com/Prash3r/TrackmaniaTwitchBot/tree/master/TTBot/optional/commands) if they are commands (message starting with !)
 - [/TTBot/optional/evaluators](https://github.com/Prash3r/TrackmaniaTwitchBot/tree/master/TTBot/optional/evaluators) if they are evaluators (all messages need to be analyzed)

## I want to implement additional functionality
Feel free to create pull requests. This is an early stage of development so if you want to implement general functionality you maybe should talk to me first - chances are that someone is already doing it. If you want to implement a command or an evaluator you should look at an existing one first.


**If you have no means of testing just commit your newmodulename.py into evaluators or commands and i will test and integrate them.**

### Some Tips and examples

 - if you need a **persistent variable** look at the evaluator [luckerscounter](https://github.com/Prash3r/TrackmaniaTwitchBot/tree/master/TTBot/optional/evaluators/EvaluatorLuckers.py) and add your variable to the PV in [_db.py](https://github.com/Prash3r/TrackmaniaTwitchBot/blob/master/TTBot/_db.py) accordingly
 - some useful functions can be found in [_tools.py](https://github.com/Prash3r/TrackmaniaTwitchBot/blob/master/TTBot/_tools.py)

### Guidelines

 1. dont commit sensitive data
 2. dont commit your local SQLite database
 3. preferrably rebase before pull request
 4. Do NOT use unsanitized ctx.content to build your sql requests - instead use the presanitized args

### Roadmap

 1. local module testing
 2. alternative SQLite interface also for local testing

### Deployment example
build docker images with appropriate tags:

    docker build -t prash3r/trackmaniatwitchbot:v0.0.1 .
    docker build -t prash3r/trackmaniatwitchbot:latest .

push docker containers to dockerhub:

    docker push prash3r/trackmaniatwitchbot:latest
	docker push prash3r/trackmaniatwitchbot:v0.0.1

then force update the running server container