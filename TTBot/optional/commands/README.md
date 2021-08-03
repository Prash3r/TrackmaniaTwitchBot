# Commands
quick usage documentation of all available module commands
## CoreCommands only accessible with core rights
### update

    !update
terminates the bot, thus the container which is restarted by the server which triggers the master branch to be pulled again. It then runs the freshly pulled bot.

### invite

    !invite
makes the bot join your channel from now on

### uninvite

    !uninvite
makes the bot not join your channel anymore. (It still is in the channel with all modules deactivated until next restart of the bot)

### module

    !module <list/add/rem> <modulename>
lets you manage the activated modules in your channel

### help

    !help <invite/uninvite/accesslevel/add/list/rem>
displays command help for the core commands
## UserCommands accessibility depends on channel settings
### mm

    !mm <trackmania2020username>
searches for trackmania2020username on trackmania.io and returns the current rank information.

### kem

    !kem
bot answers with `kem1W`

    !kem <number>
bot answers with number amout of kem1W emotes up to 10. For example `!kem 6` will be answered with `kem1W kem1W kem1W kem1W kem1W kem1W`

### joke

    !joke

tells you the biggest joke
### roll

    !roll <number>

emulates a dice of number faces and answers with the result

### score

    !score
returns a random number from 0 to 100000

