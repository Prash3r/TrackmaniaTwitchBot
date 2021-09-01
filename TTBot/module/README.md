# Commands
quick usage documentation of all available module commands

## CoreCommands only accessible with core rights
### invite
    !invite
lets the bot join your channel from now on

### uninvite
    !uninvite
lets the bot not join your channel anymore. (It still is in the channel with all modules deactivated until the next restart of the bot)

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
answers with `kem1W`

    !kem <number>
answers with number amout of kem1W emotes up to 10. For example `!kem 6` will be answered with `kem1W kem1W kem1W kem1W kem1W kem1W`

### joke
    !joke
tells you the biggest joke

### roll
    !roll <number>
emulates a dice of number faces and answers with the result

### score
    !score
returns a random number from 0 to 100000

# Evaluators
If an evaluator matches (part of) a users message, it will be executed, based on the message.
Quick usage documentation of all available module evaluators:

## luckerscounter
counts how many times someone typed "luckers" in chat (intended to count how many times the streamer LuckersTurbo was called Luckers)

## ooga
will be answered with booga

## ping
will be answered with pong