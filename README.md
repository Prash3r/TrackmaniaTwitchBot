# TTBot - Trackmania Twitch Bot
This is the repository of the [twitch.tv bot trackmania_bot](https://www.twitch.tv/trackmania_bot). Its main capability right now is that it can look up matchmaking rankings via [trackmania.io](https://trackmania.io/#/players). Additionaly there are some commands and evaluators implemented that are channel specific.

You came here for one of 3 reasons:
 - i want this bot in my channel
 - i need help configuring the bot for my needs
 - i want to implement additional functionality for other TM streamers

You came to the right place. The current version is hosted and will be pulled regurarily from this repository. There is no need to host a copy or register your own bot - although you are free to do that. 

## I want this bot in my channel
Go to the bots chat [twitch.tv bot trackmania_bot](https://www.twitch.tv/trackmania_bot) and type `!invite`

The bot will now join your channel (obviously only possible for the streamer himself). If you want the bot to leave type `!uninvite` either in the bots channel or in your own. Be mindful, this deletes all of your configuration.

## I need help configuring the bot
The basic commands `!uninvite`, `!help` and `!module` should always work and are only available for the streamer.

If you want to add an existing module you can add it via:

    !module add modulename

The functionality of the module would be available for everyone in your channel. If you only want it to be invokeable by a subset of your users you can add an accesslevel integer as 3rd argument:

    !module add modulename 5

Accesslevel 5 would mean the commands is only invokeable by subscribers.
Currently implemented access levels:

 - **100** owner of the channel
 - **10** moderators
 - **5** subscribers
 - **1** everyone

# Modules: commands and evaluators
Modules can consist of commands and/or evaluators. What commands and evaluators are exactly, and which are available, you can read up [here](https://github.com/Prash3r/TrackmaniaTwitchBot/tree/master/TTBot/module)

## I want to implement additional functionality
Feel free to create pull requests. This is an early stage of development so if you want to implement general functionality you maybe should talk to us first - chances are that someone is already doing it. If you want to implement a command or an evaluator you should look at an existing one first.

Add your new module classes to the [ModuleList](https://github.com/Prash3r/TrackmaniaTwitchBot/tree/master/TTBot/module/ModuleList.py), otherwise they cannot get executed by the bot.

### Some Tips and examples
Our best implemented module is the [karma module](https://github.com/Prash3r/TrackmaniaTwitchBot/tree/master/TTBot/module/karma), which includes one Command !karma (where you can also set the streamers karma) and one evaluator.

### Guidelines
 1. write new code in a personal fork (preferably even in an additional branch)
 2. test your new code in the avaiable offline mode (execute ./test.py)
 3. write a unittest to your new code (or at least notify us to write one, we are willing to help you out)
 4. dont commit sensitive data
 5. preferrably rebase before creating your pull request

### Deployment example
#### run.sh unchanged
If there was no change in run.sh a simple
    !update
by an authorized user will be enough to make the server pull the current master branch and run it. The docker container is version independent now.

#### run.sh changed
build docker images with appropriate tags:

    docker build -t prash3r/trackmaniatwitchbot:v0.0.1 .
    docker build -t prash3r/trackmaniatwitchbot:latest .

push docker containers to dockerhub:

    docker push prash3r/trackmaniatwitchbot:latest
	docker push prash3r/trackmaniatwitchbot:v0.0.1

then force update the running server container